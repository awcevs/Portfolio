<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<%
//세션에 랜덤 문자열 인증코드 저장
String answer = (String)session.getAttribute("code");
out.print(answer);
%>