<%@page import="java.lang.reflect.Member"%>
<%@page import="javax.management.MBeanAttributeInfo"%>
<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<%@ page import="jsp.member.model.MemberDAO" %>    
<%@ page import="jsp.member.model.MemberBean" %>
<%@ page import="java.util.ArrayList" %>
<html>
<head>
    <title>���� �������� ���ȭ��</title>
    <link href='../../css/join_style.css' rel='stylesheet' style='text/css'/>
  
    <%
    request.setCharacterEncoding("euc-kr");
	String id = request.getParameter("id");
	
	
	//DB�� ����� ȸ�������� ��� ��������
	
	MemberDAO dao = new MemberDAO();    
        // ���ǿ� ����� ���̵� �����ͼ�
        // �� ���̵� �ش��ϴ� ȸ�������� �����´�.
      MemberBean mb = dao.getUserInfo(id); 
    // memberBean = dao.getUserInfo(id);
    %>
    <script type="text/javascript">
    
        function changeForm(val){
            if(val == "-1"){
                history.back();
            }else if(val == "0"){
            	location.href="ModifyForm.jsp?id=<%=mb.getId()%>";
            
            }else if(val == "1"){
                location.href="DeleteForm.jsp?id=<%=mb.getId()%>";
                
            }
        }
        
    </script>
    
</head>
<body>
	
	
    
 <div id="wrap"> 
       
        <b><font size="6" color="gray">ȸ�� ����</font></b>
      
                        <!-- ������ ȸ�������� ����Ѵ�. -->
            <form method="post" action="../view/ModifyForm.jsp" name="Info">       
        <table>
            <tr>
                <td id="title">���̵�</td>
                <td><%=mb.getId()%></td>
            </tr>
                      
            <tr>
                <td id="title">�̸���</td>
                <td>
                    <%=mb.getMail1() %>@
                    <%=mb.getMail2() %>
                </td>
            </tr>
                    
            <tr>
                <td id="title">�޴���ȭ</td>
                <td><%=mb.getPhone() %></td>
            </tr>
            <tr>
                <td id="title">�ּ�</td>
                <td><%=mb.getAddress()%></td>
            </tr>
            </table>
            <br>
             <input type="button" value="�ڷ�" onclick="changeForm(-1)">
             <input type="button" value="ȸ����������" onclick="changeForm(0)">
       
             <input type="button" value="ȸ��Ż��" onclick="changeForm(1)">
         
        
        </form>
         </div> 
        <br>
        
</body>
</html>
