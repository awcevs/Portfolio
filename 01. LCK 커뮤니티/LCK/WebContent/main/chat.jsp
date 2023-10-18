<%@ page language="java" contentType="text/json; charset=utf-8"
    pageEncoding="utf-8"%>
<%@ page import="cteam.dao.*" %>
<%@ page import="cteam.dto.*" %>
<%@ page import="cteam.vo.*" %>
<%@ page import="java.util.ArrayList" %>
<%
UserVO login = (UserVO)session.getAttribute("login");
String  todo = request.getParameter("todo");
if(todo == null)
{
	response.sendRedirect("index.jsp");
}
ChatDTO cdto = new ChatDTO();


//채팅 insert
if(todo.equals("send"))
{
	String id = login.getId();
	String cnote = request.getParameter("cnote");
	cnote = cnote.replace("<", "&lt;");
	cnote = cnote.replace(">", "&gt;");
	
	
	if(cnote == null || cnote.equals("")) return;
	
	ChatVO cvo = new ChatVO();
	cvo.setId(id);
	cvo.setCnote(cnote);
	
	cdto.Insert(cvo);
}

//채팅 read
if(todo.equals("get"))
{
	//cno부터의 채팅 리스트 가져옴
	String cno = request.getParameter("cno");
	if(cno == null || cno.equals(""));
	{
		cno = "0";
	}
	ArrayList<ChatVO> cList = cdto.List(cno);
	//System.out.println(cList.size());
	%>
	[
		<%
		for(ChatVO cvo : cList)
		{
			String cnote = cvo.getCnote();
			cnote = cnote.replace("\"", "\\\"");
			cnote = cnote.replace("\\", "\\\\");
			//System.out.println(cnote);
			%>
			{
				"cno" : "<%= cvo.getCno() %>",
				"nick" : "<%= cvo.getNick() %>",
				"cnote" : "<%= cnote%>"
			}
			<%
			if(cList.indexOf(cvo) != cList.size()-1)
			{
				%>,<%
			}
		}
		%>
	]
	<%
}

//test
if(todo.equals("test"))
{
	String cno = request.getParameter("cno");
	ChatVO cvo = cdto.Read(cno);
	out.print(cvo.getCnote());
}
%>