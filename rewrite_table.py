import re

with open('common-component/elementary-technology/proxy-service.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if line.startswith('# 프록시서비스'):
        lines[i] = ''
    elif 'proxySvcDAO.selectProxySvcListTotCnt' in line and line.endswith(' \n'):
        lines[i] = line.rstrip() + '\n'
        
    if '| Controller | egovframework' in line:
        lines[i] = '| Controller | egovframework.com.utl.sys.pxy.web.EgovProxySvcController.java | 정보관리 컨트롤러 |\n'
    elif '| Service | egovframework' in line:
        lines[i] = '| Service | egovframework.com.utl.sys.pxy.service.EgovProxySvcService.java | 정보관리 인터페이스 |\n'
    elif '| ServiceImpl | egovframework' in line:
        lines[i] = '| ServiceImpl | egovframework.com.utl.sys.pxy.service.impl.EgovProxySvcServiceImpl.java | 정보관리 서비스 구현체 |\n'
    elif '| DAO | egovframework' in line:
        lines[i] = '| DAO | egovframework.com.utl.sys.pxy.service.impl.ProxySvcDAO.java | 정보관리 DAO |\n'
    elif '| Model | egovframework.com.utl.sys.pxy.service.ProxySvc.java' in line:
        lines[i] = '| Model | egovframework.com.utl.sys.pxy.service.ProxySvc.java | 정보관리 모델 |\n'
    elif '| Model | egovframework.com.utl.sys.pxy.service.ProxyLog.java' in line:
        lines[i] = '| Model | egovframework.com.utl.sys.pxy.service.ProxyLog.java | 로그관리 모델 |\n'
    elif '| VO | egovframework.com.utl.sys.pxy.service.ProxySvcVO.java' in line:
        lines[i] = '| VO | egovframework.com.utl.sys.pxy.service.ProxySvcVO.java | 정보관리 VO |\n'
    elif '| VO | egovframework.com.utl.sys.pxy.service.ProxyLogVO.java' in line:
        lines[i] = '| VO | egovframework.com.utl.sys.pxy.service.ProxyLogVO.java | 로그관리 VO |\n'
    elif '| JSP | /WEB-INF/jsp/egovframework/com/utl/sys/pxy/EgovProxyLogList.jsp' in line:
        lines[i] = '| JSP | /WEB-INF/jsp/egovframework/com/utl/sys/pxy/EgovProxyLogList.jsp | 로그조회 화면 |\n'
    elif '| JSP | /WEB-INF/jsp/egovframework/com/utl/sys/pxy/EgovProxySvcList.jsp' in line:
        lines[i] = '| JSP | /WEB-INF/jsp/egovframework/com/utl/sys/pxy/EgovProxySvcList.jsp | 목록조회 화면 |\n'
    elif '| JSP | /WEB-INF/jsp/egovframework/com/utl/sys/pxy/EgovProxySvcDetail.jsp' in line:
        lines[i] = '| JSP | /WEB-INF/jsp/egovframework/com/utl/sys/pxy/EgovProxySvcDetail.jsp | 상세조회 화면 |\n'
    elif '| JSP | /WEB-INF/jsp/egovframework/com/utl/sys/pxy/EgovProxySvcRegist.jsp' in line:
        lines[i] = '| JSP | /WEB-INF/jsp/egovframework/com/utl/sys/pxy/EgovProxySvcRegist.jsp | 등록 화면 |\n'
    elif '| JSP | /WEB-INF/jsp/egovframework/com/utl/sys/pxy/EgovProxySvcUpdt.jsp' in line:
        lines[i] = '| JSP | /WEB-INF/jsp/egovframework/com/utl/sys/pxy/EgovProxySvcUpdt.jsp | 수정 화면 |\n'
    elif '| Query XML | resources/egovframework/mapper/com/utl/sys/pxy/EgovProxySvc_SQL_altibase.xml' in line:
        lines[i] = '| Query XML | resources/.../EgovProxySvc_SQL_altibase.xml | Altibase용 Query XML |\n'
    elif '| Query XML | resources/egovframework/mapper/com/utl/sys/pxy/EgovProxySvc_SQL_cubrid.xml' in line:
        lines[i] = '| Query XML | resources/.../EgovProxySvc_SQL_cubrid.xml | Cubrid용 Query XML |\n'
    elif '| Query XML | resources/egovframework/mapper/com/utl/sys/pxy/EgovProxySvc_SQL_maria.xml' in line:
        lines[i] = '| Query XML | resources/.../EgovProxySvc_SQL_maria.xml | MariaDB용 Query XML |\n'
    elif '| Query XML | resources/egovframework/mapper/com/utl/sys/pxy/EgovProxySvc_SQL_mysql.xml' in line:
        lines[i] = '| Query XML | resources/.../EgovProxySvc_SQL_mysql.xml | MySQL용 Query XML |\n'
    elif '| Query XML | resources/egovframework/mapper/com/utl/sys/pxy/EgovProxySvc_SQL_oracle.xml' in line:
        lines[i] = '| Query XML | resources/.../EgovProxySvc_SQL_oracle.xml | Oracle용 Query XML |\n'
    elif '| Query XML | resources/egovframework/mapper/com/utl/sys/pxy/EgovProxySvc_SQL_postgres.xml' in line:
        lines[i] = '| Query XML | resources/.../EgovProxySvc_SQL_postgres.xml | PostgreSQL용 Query XML |\n'
    elif '| Query XML | resources/egovframework/mapper/com/utl/sys/pxy/EgovProxySvc_SQL_tibero.xml' in line:
        lines[i] = '| Query XML | resources/.../EgovProxySvc_SQL_tibero.xml | Tibero용 Query XML |\n'
    elif '| Query XML | resources/egovframework/mapper/com/utl/sys/pxy/EgovProxySvc_SQL_goldilocks.xml' in line:
        lines[i] = '| Query XML | resources/.../EgovProxySvc_SQL_goldilocks.xml | Goldilocks용 Query XML |\n'
    elif '| Validator Rule XML | resources/egovframework/validator/validator-rules.xml' in line:
        lines[i] = '| Validator Rule | resources/egovframework/validator/validator-rules.xml | Validator Rule XML |\n'
    elif '| Validator XML | resources/egovframework/validator/com/utl/sys/pxy/EgovProxySvc.xml' in line:
        lines[i] = '| Validator XML | resources/.../validator/com/utl/sys/pxy/EgovProxySvc.xml | Validator XML |\n'
    elif '| Message properties | resources/egovframework/message/com/utl/sys/pxy/message_en.properties' in line:
        lines[i] = '| Message prop | resources/.../message/com/utl/sys/pxy/message_en.properties | 영문 Message |\n'
    elif '| Message properties | resources/egovframework/message/com/utl/sys/pxy/message_ko.properties' in line:
        lines[i] = '| Message prop | resources/.../message/com/utl/sys/pxy/message_ko.properties | 한글 Message |\n'
    elif '| Idgen XML | resources/egovframework/spring/com/idgn/context-idgn-ProxySvc.xml' in line:
        lines[i] = '| Idgen XML | resources/.../spring/com/idgn/context-idgn-ProxySvc.xml | Idgen XML |\n'

    # Remove trailing spaces
    lines[i] = lines[i].rstrip() + '\n'
        
with open('common-component/elementary-technology/proxy-service.md', 'w', encoding='utf-8') as f:
    f.writelines(lines)
