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
    
    <title>회원정보 수정화면</title>
    
  
    
    <script type="text/javascript">
    
        function init(){
            setComboValue("<%=mb.getMail2()%>");
        }
 
        function setComboValue(val) 
        {
            var selectMail = document.getElementById('mail2'); // select 아이디를 가져온다.
            for (i = 0, j = selectMail.length; i < j; i++)  // select 하단 option 수만큼 반복문 돌린다.
            {
                if (selectMail.options[i].value == val)  // 입력된값과 option의 value가 같은지 비교
                {
                    selectMail.options[i].selected = true; // 같은경우라면 체크되도록 한다.
                    break;
                }
            }
        }
        
        // 비밀번호 입력여부 체크
        function checkValue() {
            if(!document.userInfo.password.value){
                alert("비밀번호를 입력하세요.");
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
       
        <b><font size="6" color="gray">회원정보 수정</font></b>
        
        
        <!-- 입력한 값을 전송하기 위해 form 태그를 사용한다 -->
        <!-- 값(파라미터) 전송은 POST 방식 -->
        <form method="post" action="../pro/ModifyPro.jsp" 
                name="userInfo" onsubmit="return checkValue()">
                
            <table>
                <tr>
                    <td id="title">아이디</td>
                    <td> <input type="text" name="id" maxlength="50" 
                            value= "<%=mb.getId()%>" readonly></td>
                </tr>
                <tr>
                    <td id="title">비밀번호</td>
                    <td>
                        <input type="password" name="password" maxlength="50" 
                            value="<%=mb.getPassword()%>">
                    </td>
                </tr>
            </table>    
            <br><br>    
            <table>
 
                <tr>
                    <td id="title">이름</td>
                    <td><input type="text" name="name" size = "50" maxlength="50" 
                            value="<%=mb.getName()%> "></td>
                </tr>
                    
                <tr>
                    <td id="title">성별</td>
                    <td><%=mb.getGender()%></td>
                </tr>
                    
                <tr>
                    <td id="title">생일</td>
                    <td>
                    <input type="text" name="birthyy" size = "15" value="<%=mb.getBirthyy() %>" placeholder="년(4자)">
						<input type="text" name="birthmm" size = "15" value="<%=mb.getBirthmm() %>" placeholder="월">
						<input type="text" name="birthdd" size = "15" value="<%=mb.getBirthdd() %>"placeholder="일">
                        
                    </td>
                </tr>
                    
                <tr>
                    <td id="title">이메일</td>
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
                    <td id="title">휴대전화</td>
                    <td>
                        <input type="text" size = "50"  name="phone" value="<%=mb.getPhone() %>"/>
                    </td>
                </tr>
                <tr>
                    <td id="title">주소</td>
                    <td>
                        <input type="text" size="50" name="address"
                            value="<%=mb.getAddress() %>"/>
                    </td>
                </tr>
            </table>
            <br>
            <input type="button" value="취소" onclick="history.back()"/>
            <input type="submit" value="수정" onclick="submitclick"/>  
        </form>
        </div>
        <br>
</body>
</html>
