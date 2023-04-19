<%@ page language="java" contentType="text/html; charset=euc-kr"
    pageEncoding="EUC-KR"%>
<%@ page import="jsp.member.model.MemberDAO" %>    
<%@ page import="jsp.member.model.MemberBean" %>
<html>
<head>
	<link href='../../css/join_style.css' rel='stylesheet' style='text/css'/>	
    <%
    request.setCharacterEncoding("euc-kr");
        String id = request.getParameter("id");
    	
         MemberDAO dao = new MemberDAO();
        
        MemberBean mb = dao.getUserInfo(id);

   
    	
    %>
    
    <title>ȸ������ ����ȭ��</title>
    
  
    
    <script type="text/javascript">
    
        function init(){
            setComboValue("<%=mb.getMail2()%>");
        }
 
        function setComboValue(val) 
        {
            var selectMail = document.getElementById('mail2'); // select ���̵� �����´�.
            for (i = 0, j = selectMail.length; i < j; i++)  // select �ϴ� option ����ŭ �ݺ��� ������.
            {
                if (selectMail.options[i].value == val)  // �ԷµȰ��� option�� value�� ������ ��
                {
                    selectMail.options[i].selected = true; // ��������� üũ�ǵ��� �Ѵ�.
                    break;
                }
            }
        }
        
        // ��й�ȣ �Է¿��� üũ
        function checkValue() {
            if(!document.userInfo.password.value){
                alert("��й�ȣ�� �Է��ϼ���.");
                return false;
            }
        function submitclick(){
        	location.href="history.back()?id=<%=mb.getId()%>";
        } 
      
        }
        
    </script>
    
</head>

<body onload="init()">
 		<div id="wrap">
       
        <b><font size="6" color="gray">ȸ������ ����</font></b>
        
        
        <!-- �Է��� ���� �����ϱ� ���� form �±׸� ����Ѵ� -->
        <!-- ��(�Ķ����) ������ POST ��� -->
        <form method="post" action="../pro/ModifyPro.jsp" 
                name="userInfo" onsubmit="return checkValue()">
                
            <table>
                <tr>
                    <td id="title">���̵�</td>
                    <td> <input type="text" name="id" maxlength="50" 
                            value= "<%=mb.getId()%>" readonly></td>
                </tr>
                <tr>
                    <td id="title">��й�ȣ</td>
                    <td>
                        <input type="password" name="password" maxlength="50" 
                            value="<%=mb.getPassword()%>">
                    </td>
                </tr>
            </table>    
            <br><br>    
            <table>
 
                <tr>
                    <td id="title">�̸�</td>
                    <td><input type="text" name="name" size = "50" maxlength="50" 
                            value="<%=mb.getName()%> "></td>
                </tr>
                    
                <tr>
                    <td id="title">����</td>
                    <td><%=mb.getGender()%></td>
                </tr>
                    
                <tr>
                    <td id="title">����</td>
                    <td>
                    <input type="text" name="birthyy" size = "15" value="<%=mb.getBirthyy() %>" placeholder="��(4��)">
						<input type="text" name="birthmm" size = "15" value="<%=mb.getBirthmm() %>" placeholder="��">
						<input type="text" name="birthdd" size = "15" value="<%=mb.getBirthdd() %>"placeholder="��">
                        
                    </td>
                </tr>
                    
                <tr>
                    <td id="title">�̸���</td>
                    <td>
                        <input type="text" name="mail1"  maxlength="50" 
                            value="<%=mb.getMail1() %>">
                        @
                        <select name="mail2" id="mail2" >
                            <option value="naver.com">naver.com</option>
                            <option value="gmail.com">gmail.com</option>
                            <option value="daum.net" >daum.net</option>
                            <option value="nate.com">nate.com</option>                        
                        </select>
                    </td>
                </tr>
                    
                <tr>
                    <td id="title">�޴���ȭ</td>
                    <td>
                        <input type="text" size = "50"  name="phone" value="<%=mb.getPhone() %>"/>
                    </td>
                </tr>
                <tr>
                    <td id="title">�ּ�</td>
                    <td>
                        <input type="text" size="50" name="address"
                            value="<%=mb.getAddress() %>"/>
                    </td>
                </tr>
            </table>
            <br>
            <input type="button" value="���" onclick="history.back()"/>
            <input type="submit" value="����" onclick="submitclick"/>  
        </form>
        </div>
        <br>
</body>
</html>
