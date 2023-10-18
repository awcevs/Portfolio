<%@ page language="java" contentType="text/html; charset=utf-8"
    pageEncoding="utf-8"%>
<%@ page import="cteam.dao.*" %>
<%@ page import="cteam.dto.*" %>
<%@ page import="cteam.vo.*" %>
<%@ page import="java.util.*" %>
<%
String menu = request.getParameter("menu");
int PageNo = 1; 
try
{
	PageNo = Integer.parseInt(request.getParameter("page"));
}catch (Exception e){}

BoardDTO bdto = new BoardDTO();
ArrayList<BoardVO> blist = new ArrayList<BoardVO>(); 
blist = bdto.List(menu, PageNo);

for(BoardVO bvo : blist)
{
	%>
	<tr>
		<td>
			<%
			switch(menu)
			{
			case "H" :
				if(!bvo.getYoutube().equals(""))
				{	
					%>
					<img src="https://img.youtube.com/vi/<%= bvo.getYoutube() %>/maxresdefault.jpg" class="thumbnail">
					<%
				}
				break;
			case "M" : 	
				if(!bvo.getBfname().equals(""))
				{
					%>
					<img src="file.jsp?bno=<%= bvo.getBno() %>" style="width:120px;height:90px" class="thumbnail">
					<%
				}
				break;
			default :
				%>
				<%= bvo.getBno() %>
				<%
				break;
			}
			
			%>
		</td>
		<td style="text-align:left;padding:5px">
			<%
			if(Integer.parseInt(bvo.getBlcount()) < 11)
			{
				%>
				<a href="view.jsp?menu=<%= menu %>&bno=<%= bvo.getBno() %>">
					<%
					if(bvo.getRcount().equals("0")) 
					{
						%><%= bvo.getBtitle() %><%
					}else
					{
						%><%= bvo.getBtitle() %> <span class="fontcolor">(<%= bvo.getRcount() %>)</span><%
					}
					%>
				</a>
				<%
			}else
			{
				%>
				<b>신고가 누적된 글입니다.</b> <a href="view.jsp?menu=<%= menu %>&bno=<%= bvo.getBno() %>">[내용보기]</a>
				<%
			}
			%>
		</td>
		<td><span class="font<%= bvo.getTeam() %>">[<%= bvo.getTeam() %> <%= bvo.getPosition() %>]</span><%= bvo.getNick() %></td>
		<td><%= bvo.getGcount() %></td>
		<td><%= bvo.getHit() %></td>
		<td><%= bvo.getWdate() %></td>
	</tr>
	<%
}
%>