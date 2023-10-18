<%@ page language="java" contentType="text/html; charset=utf-8"
    pageEncoding="utf-8"%>
<%@ include file="../include/header.jsp" %>
<%
String menu = request.getParameter("menu");
String menuname = "";
if(menu == null)
{
	response.sendRedirect("../main/index.jsp");
	return;
}

if(login == null)
{
	response.sendRedirect("../board/list.jsp?menu=" + menu);
	return;
}

%>
<script>
	window.onload = function()
	{
		$("#btitle").focus();
		
		$("#writefrm").submit(function(){
			
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
			if($("#youtube").val() != "" && $("#youtube").val().length != 11)
			{
				yid = youtube($("#youtube").val());
				if(yid.length != 11)
				{
					alert("잘못된 URL입니다.");
					return false;
				}
				$("#youtube").val(yid);
			}
			*/

			return true;
		});
		
		
		$("#btncancle").click(function(){
			if(confirm("글쓰기를 취소하시겠습니까?") == true) document.location = "list.jsp?menu=<%= menu %>";
		});
		
		//메뉴 선택 따라서 폼 변경
		$("#menu").on("change", function(){
			switch($(this).val())
			{
				default :
					$("#attachname").html("첨부파일");
					$("#attachinput").html("<input type='file' name='attach' id='attach' style='width:98%;height:25px' accept='image/*'>");
					break;
					
				case "N" :
					$("#attachname").html("기사 URL");
					$("#attachinput").html("<input type='text' name='newslink' id='newslink' style='width:98%;height:20px'>");
					break;
				
				case "H" :
					$("#attachname").html("유튜브 URL");
					$("#attachinput").html("<input type='text' name='youtube' id='youtube' style='width:98%;height:20px'>");
					break;
				
			}
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
<div style="margin: 0px 0px 0px 50px"><h1>글작성</h1></div>
<br>
<form name="writefrm" id="writefrm" action="writeok.jsp" method="post" enctype="multipart/form-data">
	<table align="center" class="tableline" style="width:860px;text-align:center;margin:0px 50px 0px 50px">
		<tr>
			<td style="width:120px;height:20px">제목</td>
			<td colspan="3">
				<input type="text" name="btitle" id="btitle" placeholder="제목을 입력하세요.(최대 40글자)" style="width:758px;height:20px;margin:0px;padding:0px" maxlength="40">
			</td>
		</tr>
		<tr>
			<td>게시판 선택</td>
			<td style="width:120px">
				<select name="menu" id="menu" style="height:20px">
					<option <%= menu.equals("N") ? "selected" : "" %> value="N">뉴스 기사</option>
					<option <%= menu.equals("T") ? "selected" : "" %> value="T">대회 이야기</option>
					<option <%= menu.equals("H") ? "selected" : "" %> value="H">대회 하이라이트</option>
					<option <%= menu.equals("F") ? "selected" : "" %> value="F">자유 주제</option>
					<option <%= menu.equals("Q") ? "selected" : "" %> value="Q">질문 & 답변</option>
					<option <%= menu.equals("I") ? "selected" : "" %> value="I">정보 & 팁</option>
					<option <%= menu.equals("P") ? "selected" : "" %> value="P">파티 모집</option>
					<option <%= menu.equals("M") ? "selected" : "" %> value="M">이미지</option>
				</select>
			</td>
			<%
			if(menu.equals("N"))
			{
				%>
				<td style="width:120px"><div id="attachname">기사 URL</div></td>
				<td style="height:30px">
					<div id="attachinput">
						<input type="text" name="newslink" id="newslink" style="width:98%;height:20px">
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
						<input type="text" name="youtube" id="youtube" style="width:98%;height:20px">
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
						<input type="file" name="attach" id="attach" style="width:98%;height:25px" accept="image/*">
					</div>
				</td>
				<%
			}
			%>
		</tr>
		<tr>
			<td colspan="4">
				<textarea rows="30" name="bnote" id="bnote" style="padding:10px;width:860px;resize: none" placeholder="최대 200자까지 입력 가능합니다." maxlength="200" ></textarea>
			</td>
		</tr>
	</table>
	<br>
	<div align="center">
		<button type="submit" class="btnblue" name="btnwrite" id="btnwrite" style="margin:0px 150px 0px 0px; width:80px; height:30px">작성</button> 
		<button type="button" class="btnorange" name="btncancle" id="btncancle" style="width:80px; height:30px">취소</button>
	</div>
</form>
<br>
<!-- 컨텐츠 영역 종료 ======================================== -->
<%@ include file="../include/footer.jsp" %>