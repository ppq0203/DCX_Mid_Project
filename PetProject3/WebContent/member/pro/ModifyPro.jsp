<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<%-- �ڹٺ� Ŭ���� import --%>      
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
    <title>ȸ������ ����ó��</title>
</head>
<body>
    <%-- �ڹٺ� ���� �׼��±� ��� --%>
    <jsp:useBean id="memberBean" class="jsp.member.model.MemberBean" />
    <jsp:setProperty property="*" name="memberBean"/>    
    
    <%
    request.setCharacterEncoding("euc-kr");
        // ���ǿ��� ���̵� ������ MemberBean�� �����Ѵ�.
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
        
        // ������ ȸ�������� ����ִ� MemberBean�� DAO�� �����Ͽ� ȸ������ ������ �Ѵ�.
        MemberDAO dao = MemberDAO.getInstance();
        dao.updateMember(memberBean);
        
    %>
    
    
    <br><br>
    <font size="5" color="gray">ȸ�������� �����Ǿ����ϴ�.</font>
    <br><br>
    <input type="button" value="��������" onclick="goLogForm()"/>
    
</body>
</html>
