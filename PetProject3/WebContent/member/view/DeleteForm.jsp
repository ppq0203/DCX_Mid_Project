<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
    <%@ page import="jsp.member.model.MemberBean" %>
<html>
<head>
    <title>Ż�� ȭ��</title>
    
    <link href='../../css/join_style.css' rel='stylesheet' style='text/css'/>
     <jsp:useBean id="dao" class="jsp.member.model.MemberDAO" />
     <%
     request.setCharacterEncoding("euc-kr");
     String id = request.getParameter("id");
     System.out.println("id= " + id);
    MemberBean mb = dao.getUserInfo(id);
     
     
     %>
    <script type="text/javascript">
        // ��й�ȣ ���Է½� ���â
       
      
        
        function checkValue(){
            if(!document.deleteform.password.value){
                alert("��й�ȣ�� �Է����� �ʾҽ��ϴ�.");
                return false;
            }
            
    </script>
    
</head>
<body>
 	<div id="wrap"> 
    <br><br>
    <b><font size="6" color="gray">ȸ�� ����</font></b>
    <br><br><br>
 
    <form name="deleteform" method="get" action="../pro/DeletePro.jsp"
        onsubmit="return checkValue()">
 
        <table>
        <tr>
                <td bgcolor="skyblue">���̵�</td>
                <td><input type="text" name="id" maxlength="50" value = "<%=mb.getId()%>" readonly></td>
            </tr>
            <tr>
                <td bgcolor="skyblue">��й�ȣ</td>
                <td><input type="password" name="password" maxlength="50"></td>
            </tr>
        </table>
        
        <br> 
        <input type="button" value="���" onclick="history.back()"/>
        <input type="submit" value="Ż��"/> 
    </form>
    </div>
</body>
</html>
