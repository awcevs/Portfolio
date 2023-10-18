<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<%@ page import="cteam.dao.*" %>
<%@ page import="cteam.dto.*" %>
<%@ page import="java.util.*" %>
<%@ page import="cteam.vo.*" %>
<%
String email = request.getParameter("usermail");
UserDTO dto = new UserDTO();
//회원가입 시 입력한 이메일 보내기
dto.IpEmail(email);

response.sendRedirect("userlogin.jsp");


%>