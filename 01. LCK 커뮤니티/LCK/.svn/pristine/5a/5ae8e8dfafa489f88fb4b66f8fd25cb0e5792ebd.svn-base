<%@ page language="java" contentType="text/html; charset=utf-8"
    pageEncoding="utf-8"%>
<%@ page import="cteam.dao.*" %>
<%@ page import="cteam.dto.*" %>
<%@ page import="cteam.vo.*" %>
<%@ page import="java.util.*" %>
<%
String menu = request.getParameter("menu");
int pageNo = 1;
try
{
	pageNo = Integer.parseInt(request.getParameter("pageNo"));
}catch(Exception e){};
String opt  = request.getParameter("opt");
String word = request.getParameter("word");

BoardDTO bdto = new BoardDTO();
ArrayList<BoardVO> blist = bdto.ListSearch(menu, pageNo, opt, word);
%>
