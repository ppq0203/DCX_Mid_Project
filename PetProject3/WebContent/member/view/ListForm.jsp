<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<%@ page import="jsp.member.model.MemberDAO" %>    
<%@ page import="jsp.member.model.MemberBean" %>
<%@ page import="java.util.ArrayList" %>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>


<%
	//로그인 체크
	//로그인을 안했거나, admin이 아니면 로그인으로 이동하는 로직
	request.setCharacterEncoding("euc-kr");
	String id = (String)session.getAttribute("id");
	
	
	//DB에 저장된 회원정보를 모두 가져오기
	
	//MemberDAO 객체 생성 
	MemberDAO dao = new MemberDAO();
	
	//dao객체 안에 회원정보 전부를 조회하는 메서드 호출 
	ArrayList member = dao.memberList();
	
	System.out.print(member);
	//정보 출력
	
	%>
<body>
<table border ="1">
	 <tr>
	 	<td>아이디</td>
	 	<td>비밀번호</td>
	 	<td>이름</td>
	 	<td>성별</td>
	 	<td>이메일</td>
	 	<td>가입일</td>
	 </tr>
	 <%for(int i = 0;i<member.size();i++) {
			MemberBean mb = (MemberBean)member.get(i);
		 %>    
	 	<tr>
	 	<td><a href="UserInfo.jsp?id=<%=mb.getId() %>">
	 	<%=mb.getId() %></a></td>
	 	<td><%=mb.getPassword()%></td>
	 	<td><%=mb.getName() %></td>
	 	<td><%=mb.getGender() %></td>
	 	<td><%=mb.getMail1()%>@<%=mb.getMail2()%></td>
	 	<td><%=mb.getReg()%></td>
	 </tr>
	<%} %>
	</table>
		
	<a href ="../../MainForm.jsp"> 메인페이지 </a>
</body>
</html>