<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<%-- 자바빈 클래스 import --%>      
<%@ page import="jsp.member.model.MemberBean" %>  
<%-- DAO import --%>   
<%@ page import="jsp.member.model.MemberDAO" %> 
    
<html>
<head>
<script>
function goLogForm() {
	location.href="../view/ListForm.jsp?id=<%=session.getAttribute("id")%>;
}	

</script>
    <title>회원정보 수정처리</title>
</head>
<body>
    <%-- 자바빈 관련 액션태그 사용 --%>
    <jsp:useBean id="memberBean" class="jsp.member.model.MemberBean" />
    <jsp:setProperty property="*" name="memberBean"/>    
    
    <%
    request.setCharacterEncoding("euc-kr");
        // 세션에서 아이디를 가져와 MemberBean에 세팅한다.
        String id= request.getParameter("id"); 
    	String pwd = request.getParameter("password");
    	String mail1 = request.getParameter("mail1");
    	String mail2 = request.getParameter("mail2");
    	String phone = request.getParameter("phone");
    	String address = request.getParameter("address");
    		
    	
        memberBean.setId(id);
        memberBean.setPw(pwd);        
        memberBean.setMail1(mail1);
        memberBean.setMail2(mail2);
        memberBean.setPhone(phone);
        memberBean.setAddress(address);
        
        // 수정할 회원정보를 담고있는 MemberBean을 DAO로 전달하여 회원정보 수정을 한다.
        MemberDAO dao = MemberDAO.getInstance();
        dao.updateMember(memberBean);
        
    %>
    
    
    <br><br>
    <font size="5" color="gray">회원정보가 수정되었습니다.</font>
    <br><br>
    <input type="button" value="메인으로" onclick="goLogForm()"/>
    
</body>
</html>
