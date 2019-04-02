#_author: llm
#_date: 2019-04-01

import os
import sys
import ldap

server = "ldap://127.0.0.1:8000"
baseDN = "dc=domainname, dc=com"
searchScope = ldap.SCOPE_SUBTREE
# 设置过滤属性， 这里只显示 cn=test 的信息
searchFilter = "sAMAccountName="
# 为用户加上域名
user_name = 'domainname\\'
# none 表示搜索所有属性， ['cn']表示只搜索 cn 属性
retrieveAttributes = None

def conn_ldap(username, password):
    global user_name
    user_name = user_name + username

    conn = ldap.initialize(server)
    conn.set_option(ldap.OPT_REFERRALS, 0)
    conn.protocol_version = ldap.VERSION3

    # 这里用户名是域帐号的全名，如 domain/name
    print(conn.simple_bind_s(user_name, password))
    print('ldap connect successfully')

    return conn

def login_ldap(username, password):
    try:
        global searchFilter
        searchFilter = searchFilter + username
        conn = conn_ldap(username, password)

        # 调用search方法返回结果id
        ldap_result_id = conn.search(baseDN, searchScope, searchFilter, retrieveAttributes)
        result_set = []
        print(ldap_result_id)

        while 1:
            result_type, result_data = conn.result(ldap_result_id, 0)
            if(result_data == []):
                break
            else:
                if result_type == ldap.RES_SEARCH_ENTRY:
                    result_set.append(result_data)

        Name, Attrs = result_set[0][0]
        if hasattr(Attrs, 'has_key') and Attrs.has_key('name'):
            print('test3')
            distinguishedName = Attrs['mail'][0]
            print('login info for user : %s' % distinguishedName)

            return distinguishedName
        else:
            print('in error')
            return None
    except ldap.LDAPError as e:
        print('out error: %s' % e)
        return None




