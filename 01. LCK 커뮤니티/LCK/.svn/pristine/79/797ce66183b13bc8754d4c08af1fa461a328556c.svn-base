<%@ page language="java" contentType="text/html; charset=utf-8"
    pageEncoding="utf-8"%>
<%@ include file="../include/header.jsp" %>
<!-- 컨텐츠 영역 시작 ======================================== -->
<%
if(login == null)
{
	response.sendRedirect("../user/userlogin.jsp");
	return;
}

String menu = request.getParameter("menu");
String bno  = request.getParameter("bno");

if(bno == null || bno.equals(""))
{
	response.sendRedirect("list.jsp?menu=" + menu);
	return;
}

BoardDTO dto = new BoardDTO();
BoardVO  vo  = dto.Read(bno, false);

if(!vo.getId().equals(login.getId()) && !(login.getUserdiv().equals("2")))
{
	response.sendRedirect("list.jsp?menu=" + menu);
	return;
}

dto.Delete(bno);

response.sendRedirect("list.jsp?menu=" + menu);

%>
<!-- 컨텐츠 영역 종료 ======================================== -->
<%@ include file="../include/footer.jsp" %>