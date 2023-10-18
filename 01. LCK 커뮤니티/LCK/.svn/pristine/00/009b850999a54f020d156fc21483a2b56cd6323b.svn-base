<%@ page language="java" contentType="text/html; charset=UTF-8""
    pageEncoding="UTF-8"%>
<%@ page import="cteam.dao.*" %>
<%@ page import="cteam.dto.*" %>
<%@ page import="cteam.vo.*" %> 
<%

request.setCharacterEncoding("UTF-8");
UserVO login = (UserVO)session.getAttribute("login");

String userpw = request.getParameter("userpw");
if(userpw == null || userpw.equals("") )
{
	out.println("ERROR");
	return;
}

UserDTO dto = new UserDTO();
if( dto.IsPuplicate(userpw,login.getId()) == true)
{
	//비밀번호 중복됨
	out.println("DUPLICATE");
}else
{
	//중복 안된 비밀번호
	out.println("NOT_DUPLICATE");
}
%>