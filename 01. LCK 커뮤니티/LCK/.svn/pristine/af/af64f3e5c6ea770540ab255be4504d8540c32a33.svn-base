<%@ page language="java" contentType="text/html; charset=utf-8"
    pageEncoding="utf-8"%>
<%@ page import="cteam.dao.*" %>
<%@ page import="cteam.dto.*" %>
<%@ page import="cteam.vo.*" %>
<%@ page import="java.util.*" %>
<%
request.setCharacterEncoding("utf-8");

//세션에 구워져있는 로그인 정보를 가져온다
UserVO login = (UserVO)session.getAttribute("login");

//modify에서 변경 가능한 목록 비밀번호, 닉네임, 팀, 포지션
String id = login.getId();
String userpw = request.getParameter("userpw");
String pw = request.getParameter("newpw");
String user = request.getParameter("user");
String userteam = request.getParameter("userteam");
String userpt = request.getParameter("userpt");

UserVO vo = new UserVO();

//로그인 정보가 없을 떄 막음
if(login == null)
{
	out.println("변경 권한이 없습니다.");
}
if(pw == null)
{
	pw = vo.getPw();
}
UserDTO dto = new UserDTO();

if( user == null)
{
	dto.Read(id);
	user = vo.getNick();
	
}
if(dto.IsPuplicate(login.getId(),userpw) == false)
{
	
		//비밀번호 변경	
		//회원정보 수정에 들어온 아이디를 통해 입력된 비밀번호가 일치하지 않을 때
		%><script>
		alert("현재 비밀번호가 일치하지 않습니다.") 
		document.location="usermodify.jsp";
		</script><%
}
else
{
	//비밀번호, 팀, 닉네임, 포지션 변경
	dto.Update(id, pw, userteam, userpt, user);
	//중복 안된 비밀번호
	%>
	<script>
	alert("회원 수정이 완료되었습니다. 다시 로그인 해주세요.");
	document.location="../main/index.jsp";
	</script>
	<%
	//세션 죽여버리는 코드
	session.invalidate();
}

%>