<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
    <%@ page import="jsp.member.model.MemberBean" %>
<html>
<head>
    <title>탈퇴 화면</title>
    
    <link href='../../css/join_style.css' rel='stylesheet' style='text/css'/>
     <jsp:useBean id="dao" class="jsp.member.model.MemberDAO" />
     <%
     request.setCharacterEncoding("euc-kr");
     String id = request.getParameter("id");
     System.out.println("id= " + id);
    MemberBean mb = dao.getUserInfo(id);
     
     
     %>
    <script type="text/javascript">
        // 비밀번호 미입력시 경고창
       
      
        
        function checkValue(){
            if(!document.deleteform.password.value){
                alert("비밀번호를 입력하지 않았습니다.");
                return false;
            }
            
    </script>
    
</head>
<body>
 	<div id="wrap"> 
    <br><br>
    <b><font size="6" color="gray">회원 정보</font></b>
    <br><br><br>
 
    <form name="deleteform" method="get" action="../pro/DeletePro.jsp"
        onsubmit="return checkValue()">
 
        <table>
        <tr>
                <td bgcolor="skyblue">아이디</td>
                <td><input type="text" name="id" maxlength="50" value = "<%=mb.getId()%>" readonly></td>
            </tr>
            <tr>
                <td bgcolor="skyblue">비밀번호</td>
                <td><input type="password" name="password" maxlength="50"></td>
            </tr>
        </table>
        
        <br> 
        <input type="button" value="취소" onclick="history.back()"/>
        <input type="submit" value="탈퇴"/> 
    </form>
    </div>
</body>
</html>
