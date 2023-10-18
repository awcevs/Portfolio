<%@ page language="java" contentType="text/html; charset=utf-8"
    pageEncoding="utf-8"%>
<%@ include file="../include/header.jsp" %>
<%

String menu = request.getParameter("menu");
String bno  = request.getParameter("bno");
if(menu == null || bno == null || bno.equals(""))
{
	response.sendRedirect("../main/index.jsp");
	return;
}

String menuname = "";
switch(menu)
{
	case "N" :
		menuname = "뉴스 기사";
		break;
	case "T" :
		menuname = "대회 이야기";
		break;
	case "H" :
		menuname = "대회 하이라이트";
		break;
	case "F" :
		menuname = "자유 주제";
		break;
	case "Q" :
		menuname = "질문 & 답변";
		break;
	case "I" :
		menuname = "정보 & 팁";
		break;
	case "P" :
		menuname = "팀원 모집";
		break;
	case "M" :
		menuname = "이미지 & 동영상";
		break;
}

BoardVO  bvo  = bdto.Read(bno, false);

if(!bvo.getId().equals(id) && !(login.getUserdiv().equals("2")))
{
	response.sendRedirect("../main/index.jsp");
	return;
}

%>
<script>
	window.onload = function()
	{
		$("#btitle").focus();
		
		$("#modifyfrm").submit(function(){
			
			if($("#btitle").val() == "")
			{
				alert("제목을 입력해주세요.");
				$("#btitle").focus();
				return false;
			}
			
			if($("#bnote").val() == "")
			{
				alert("내용을 입력해주세요.");
				$("#bnote").focus();
				return false;
			}
			
			var yid = youtube($("#youtube").val());
			
			

			$("#youtube").val(yid);
			
			/*
			var yid = youtube($("#youtube").val());

			if(yid.length != 11 || $("#youtube").val() == "")
			{
				alert("잘못된 URL입니다.");
				$("#youtube").focus();
				return false;
			}else
			{
				$("#youtube").val(yid);
			}
			*/	
		
		});
		
		$("#btncancle").click(function(){
			if(confirm("글수정을 취소하시겠습니까?") == true) document.location = "view.jsp?menu=<%= menu %>&bno=<%= bno %>";
		});
		
	}
	//유튜브 url 변환
	function youtube(url)
	{
		if(url == "")return "";
		//동영상 id 찾는 정규표현식
		var regExp = /(youtu.*be.*)\/(watch\?v=|embed\/|v|shorts|)(.*?((?=[&#?])|$))/gm;
		return regExp.exec(url)[3];
	}	

</script>
<!-- 컨텐츠 영역 시작 ======================================== -->
<div style="margin: 0px 0px 0px 50px">
	<h1>글수정</h1>
</div>
<br>
<form action="modifyok.jsp?menu=<%= menu %>&bno=<%= bno %>" name="modifyfrm" id="modifyfrm" method="post" enctype="multipart/form-data">
<table class="tableline" align="center" style="width:860px;text-align:center;margin:0px 50px 0px 50px">
	<tr>
		<td style="width:120px">제목</td>
		<td colspan="3">
			<input  maxlength="40" placeholder="제목을 입력하세요.(최대 40글자)" type="text" name="btitle" id="btitle" style="width:758px;height:20px;margin:0px;padding:0px" value="<%= bvo.getBtitle() %>">
		</td>
	</tr>
	<tr>
		<td>게시판</td>
		<td style="width:120px">
			<select name="menu" id="menu" style="height:20px">
				<option selected value="<%= menu %>"><%= menuname %></option>
			</select>
		</td>
			<%
			if(menu.equals("N"))
			{
				%>
				<td style="width:120px"><div id="attachname">기사 URL</div></td>
				<td style="height:30px">
					<div id="attachinput">
						<input type="text" name="newslink" id="newslink" value="<%= bvo.getNewslink() %>" style="width:98%;height:20px">
					</div>
				</td>
				<%
			}
			if(menu.equals("H"))
			{
				%>
				<td style="width:120px"><div id="attachname">유튜브 URL</div></td>
				<td style="height:30px">
					<div id="attachinput">
						<input type="text" name="youtube" id="youtube"
						<%
						if(bvo.getYoutube() != null)
						{
							%>value="<%= bvo.getYoutube() %>"<%
						}
						%>						
						style="width:98%;height:20px">
					</div>
				</td>
				<%
			}
			if(!menu.equals("N") && !menu.equals("H"))
			{
				%>
				<td style="width:120px"><div id="attachname">첨부파일</div></td>
				<td style="height:30px">
					<div id="attachinput">
						<input type="file" name="attach" id="attach" style="width:98%;height:25px">
					</div>
				</td>
				<%
			}
			%>
	</tr>
	<%
	if(!bvo.getBfname().equals(""))
	{
		%>
		<tr>
			<td colspan="2">수정 전 첨부파일</td>
			<td colspan="2">
				<a href="file.jsp?bno=<%= bno %>"><%= bvo.getBfname() %></a>
			</td>
		</tr>
		<%
	}
	%>
	<tr>
		<td colspan="4">
			<textarea rows="30" name="bnote" id="bnote" style="width:860px;padding:10px" maxlength="200" placeholder="최대 200자까지 입력 가능합니다."><%= bvo.getBnote() %></textarea>
		</td>
	</tr>
</table>
<br>
<div align="center">
	<button type="submit" class="btnblue" name="btnmodify" id="btnmodify" style="margin:0px 150px 0px 0px; width:80px; height:30px">수정</button> 
	<button type="button" class="btnorange" name="btncancle" id="btncancle" style="width:80px; height:30px">취소</button>
</div>
</form>
<!-- 컨텐츠 영역 종료 ======================================== -->
<%@ include file="../include/footer.jsp" %>