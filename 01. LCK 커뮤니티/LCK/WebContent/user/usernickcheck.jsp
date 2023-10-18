<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ page import="cteam.dao.*" %>
<%@ page import="cteam.dto.*" %>
<%@ page import="cteam.vo.*" %> 
<%

request.setCharacterEncoding("UTF-8");

//로그인 된 세션 
UserVO login = (UserVO)session.getAttribute("login");


//닉네임 중복 검사여서 닉네임을 받아옴
String user = request.getParameter("user");
System.out.println("user"+user);
//System.out.println("현재 닉네임"+login.getNick());

UserDTO dto = new UserDTO();


if(user == null || user.equals(""))
{
	out.println("오류");
	return;
}

//현재 닉네임 검사
if( login != null  &&  dto.IsCuplicate(user, login.getId()) == true) 
{
	out.println("현재 닉네임입니다.");
}

//유저가 변경 할 닉네임이 데이터베이스에 있을 때 "중복"
else if( dto.IsCuplicate(user) == true)
{
	//ID 중복됨
	out.println("중복");
}
else
{
	//중복 안된 ID
	out.println("중복안됨");
}

%>
