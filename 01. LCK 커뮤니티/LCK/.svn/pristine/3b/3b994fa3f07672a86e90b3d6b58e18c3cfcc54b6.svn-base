<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ page import="cteam.dao.*" %>
<%@ page import="cteam.dto.*" %>
<%@ page import="cteam.vo.*" %> 
<%

request.setCharacterEncoding("UTF-8");

String userid = request.getParameter("userid");
if(userid == null || userid.equals("") )
{
	out.println("ERROR");
	return;
}

UserDTO dto = new UserDTO();
//유저가 입력한 아이디 중복검사
if( dto.IsDuplicate(userid) == true)
{
	//ID 중복됨
	out.println("DUPLICATE");
}else
{
	//중복 안된 ID
	out.println("NOT_DUPLICATE");
}
%>
