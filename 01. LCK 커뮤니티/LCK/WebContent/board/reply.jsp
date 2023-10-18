<%@ page language="java" contentType="text/html; charset=utf-8"
    pageEncoding="utf-8"%>
<%@ page import="cteam.dao.*" %>
<%@ page import="cteam.dto.*" %>
<%@ page import="cteam.vo.*" %>
<%@ page import="java.util.*" %>

<%
String bno = request.getParameter("bno");
String todo = request.getParameter("todo");
UserVO login = (UserVO)session.getAttribute("login");
String id = null;
if(login != null) id = login.getId();
//임시 로그인 유저 수정할것

ReplyDTO rdto = new ReplyDTO();
ReplyVO  rvo  = new ReplyVO();
ArrayList<ReplyVO> rlist = rdto.List(bno);

//replywrite
if(todo.equals("write"))
{
	String rnote = request.getParameter("rnote");
	if(rnote == null || rnote.equals(""))
	{
		return;
	}
	rvo.setId(login.getId());
	rvo.setBno(request.getParameter("bno"));
	rnote = rnote.replace("<", "&lt;");
	rnote = rnote.replace(">", "&gt;");
	rnote = rnote.replace("\"", "&quot;");
	rvo.setRnote(rnote);
	rdto.Insert(rvo);
}
//replymodify
if(todo.equals("modifyfrm"))
{
	String rno = request.getParameter("rno");
	ReplyVO revo = rdto.Read(rno);
	System.out.println(rno);
	%>
	<input type="text" id="rnote" name="rnote" value="<%= revo.getRnote() %>" style="width:590px;height:20px" maxlength="60">
	<button class="btnblue" id="btnrpmodify" style="display:inline-block;float:right;width:50px;height:30px" onclick="ModifyReplyOK(this,'<%= rno %>')">변경</button>
	<%
}


if(todo.equals("modify"))
{
	String rno   = request.getParameter("rno");
	String rnote = request.getParameter("rnote");
	rnote = rnote.replace("<", "&lt;");
	rnote = rnote.replace(">", "&gt;");
	rvo.setRno(rno);
	rvo.setRnote(rnote);
	rdto.Update(rvo);
}

//replydelete
if(todo.equals("delete"))
{
	String rno = request.getParameter("rno");
	rdto.Delete(rno);
}

//replyread - 블라인드 댓글 내용 가져옴
if(todo.equals("read"))
{
	String rno = request.getParameter("rno");
	rvo = rdto.Read(rno);
	out.print(rvo.getRnote());
}

//replylist
if(todo.equals("list"))
{
	%>
	<table class="tableline" align="center" style="width:860px">
			<%
			if(login != null)
			{
				%>
				<tr>
					<td style="vertical-align:top;width:180px">
						<span class="font<%= login.getTeam() %>">[<%= login.getTeam() %> <%= login.getPosition() %>]</span><%= login.getNick() %>
					</td>
					<td>
						<input type="text" id="rnote" style="width:590px;height:20px" maxlength="30" placeholder="최대 30글자까지 입력 가능합니다.">
						<button class="btnblue" id="btnrpwrite" style="display:inline-block;float:right;width:50px;height:30px">작성</button>
					</td>
				</tr>
				<%
			}
			else
			{
				%>
				<tr>
					<td style="vertical-align:top;width:180px">
						비로그인
					</td>
					<td>
						<input type="text" style="width:650px;height:20px" value="로그인이 필요합니다." disabled>
					</td>
				</tr>
				<%
			}
		for(ReplyVO vo : rlist)
		{
			%>
			<tr>
				<td style="vertical-align:top">
					<span class="font<%= vo.getTeam() %>">[<%= vo.getTeam() %> <%= vo.getPosition() %>]</span><%= vo.getNick() %>
				</td>
				<td id="rnotetd">
					<%
					if(vo.getId().equals(id) || (login != null && login.getUserdiv().equals("2")))
					{
						%>
						<div id="rdiv<%= vo.getRno() %>">
							<%= vo.getRnote() %>
							<a href="javascript:replydelete(<%= vo.getRno() %>);"> [삭제]</a>
							<button class="btnblue" name="btnrpmodify" id="btnrpmodify" onclick="javascript:ReplyModify(this,'<%= vo.getRno() %>');" style="display:inline-block;float:right;width:50px;height:30px">수정</button>
						</div>
						<%
					}else
					{
						if(Integer.parseInt(vo.getRblcount()) < 11)
						{
							%>
							<%= vo.getRnote() %>
							<button class="btnorange" name="btnrpblind" id="btnrpblind" onclick="rpblupdate(<%= vo.getBno() %> ,<%= vo.getRno() %>)" style="display:inline-block;float:right;width:50px;height:30px">신고</button>
							<%
						}else
						{
							%>
							<span id=rpblind<%= vo.getRno() %>>신고가 누적된 댓글입니다 <a href="javascript:getblrp(<%= vo.getRno() %>);" >[댓글 보기]</a></span>
							<%
						}
					}
					%>
				</td>
			</tr>
			<%
		}
		%>
	</table>
	<%
}
%>