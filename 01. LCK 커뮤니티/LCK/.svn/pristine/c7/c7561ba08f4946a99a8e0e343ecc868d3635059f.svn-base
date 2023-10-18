<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ page import="cteam.dao.*" %>
<%@ page import="cteam.dto.*" %>
<%@ page import="cteam.vo.*" %>
<%@ page import="java.util.*" %>
<%
request.setCharacterEncoding("UTF-8");

UserVO user = new UserVO();
String id = request.getParameter("userid");
String pw = request.getParameter("userpw");
String name = request.getParameter("username");
String nick = request.getParameter("user");
String team = request.getParameter("userteam");
String position = request.getParameter("userpt");
String email = request.getParameter("usermail");
String userok = request.getParameter("userok");
user.setId(id);
user.setPw(pw);
user.setName(name);
user.setNick(nick);
user.setTeam(team);
user.setPosition(position);
user.setEmail(email);

if( user.getId() == null || user.getPw() == null || user.getName() == null || user.getNick() == null || user.getTeam() == null || user.getPosition() == null || user.getEmail() == null || userok == null)
{
	response.sendRedirect("userjoin.jsp");
	return;
}
UserDTO dto = new UserDTO();

//유저가 입력한 정보 중 아이디, 닉네임, 이메일이 중복되었으면 가입 x
if( dto.Join(user) == false)
{
	//중복된 아이디가 존재함.
		%>
		<script>
			alert("중복된 아이디 [<%= user.getId() %>]가 존재합니다.");
			document.location = "userjoin.jsp";
		</script>
		<%
}else 
{
	%>
	<script>
		alert("아이디 [<%= user.getId() %>]로 회원가입이 완료되었습니다.");
		document.location = "userlogin.jsp";
	</script>
		<% 
}
%>
