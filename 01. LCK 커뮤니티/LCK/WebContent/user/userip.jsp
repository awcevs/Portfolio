<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<%@ page import="cteam.dao.*" %>
<%@ page import="cteam.dto.*" %>
<%@ page import="cteam.vo.*" %>
<%@ page import="java.util.*" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>Insert title here</title>
<script src="../js/jquery-3.7.0.js"></script>
</head>
<body>
	<style>
	.userip_form
	{
    	width: 400px;
	    margin: auto; 
	    padding: 0 20px;
	    margin-bottom: 20px;
	}
	.userip_form b
	{
	    display: block; 
	    margin-bottom: 5px;
	}
	.userip_form input:not(input[type=test])
	{
	    border: 1px solid #dadada;
	    padding: 15px;
	    width: 100%;
	    margin-bottom: 5px;
	}
	
	.userjoin
	{
		width:33%; 
		text-align:center;
		margin: 0 auto;
		height: auto;
		float:left;
	}
	
	.useripok
	{
		width:100%; 
		float:left;
	}
	.useripcansel
	{
		width:33%; 
		float:right;
	}
	.ipjoin
	{
		width:33%; 
		float:left;
		/*border: 1px solid gold; 
		float: left; 
		width: 33%;"
		*/
	}
	.ipcansel
	{
		width:33%;
		float: right;
		/*
		border: 1px solid gold; 
		float: left; 
		width: 33%;
		*/
	}
	</style>
	<script>
	
	var checkCode = "ERROR";
	
	
	
	window.onload = function()
	{
		$("#usermail").focus();
		
		//발송 button 형식의 id 값
		$("#sendId").click(function(){
			
			var usermail = 	$("#usermail").val();
			var code="";
			if(!email_check(usermail))
			{
				alert("이메일 형식에 맞게 입력해주세요");
				$("#usermail").focus();
				return false;
			}
			
			 //alert("tet");
			if($("#usermail").val() == "")
			{
				alert("이메일을 입력하세요");
				$("#usermail").focus();
				return false;
			}
			
			$.ajax({
				type : "post",
				url: "emailicheck.jsp",
				data: {"usermail": usermail},
				dataType: "html", //html,xml,json 셋 중 데이터 타입을 정할 수 있음
				success : function(data) 
				{
				//alert(data.length);
				code ="<%=session.getAttribute("code")%>";
			//alert(data);
			//	alert(code);
					alert("이메일로 인증코드를 보냈습니다.");
				},
				error : function(){
					alert("인증코드 전송 오류입니다");
				}
			});				

			});
		
		$("#sendcode").click(function(){
			
			$.ajax({
				type : "get",
				url: "getcode.jsp",
				dataType: "html",
				success : function(data) 
				{	
					// 통신이 성공적으로 이루어졌을때 이 함수를 타게된다.
					//String code = (String)session.getAttribute("code");
					data = data.trim();					
					console.log(data);
					if($("#usercode").val() != data)
					{
						alert("가입코드가 일치 하지 않습니다.");
						$("#usercode").focus();
					}else
					{		alert("아이디와 비밀번호가 전송되었습니다.");
							//$("#joinFrm").submit();
							document.ipFrm.submit();
							document.location = "userlogin.jsp";
							window.close();
					}
				},
				error : function(xhr, status, error) 
				{
					// 통신 오류 발생시
				}
			});
		});
		
	}
	
	
	function email_check(usermail) 
	{

		var reg = /^[0-9a-zA-Z]([-_\.]?[0-9a-zA-Z])*@[0-9a-zA-Z]([-_\.]?[0-9a-zA-Z])*\.[a-zA-Z]{2,3}$/i;

		return reg.test(usermail);

	}
	
	</script>
	<center><img src="../images/logo2.png"></center>
	<form action="emailip.jsp" method="post" id="ipFrm" name="ipFrm">
		<div class="userip_form">
			<div class="fild">
			<b>이메일</b>
			<input class="usermail" type="text" id="usermail" name="usermail" placeholder="회원가입시 사용한 이메일을 입력해주세요.">
			</div>
			<div class="useripok">
			<input class="ipcansel" type="button" value="발송" id="sendId">
			</div>
			<br>
			<br>
			<br>
			<div class="fild">
			<b>인증번호</b>
			<input class="usercode" type="text" id="usercode" name="usercode" placeholder="인증코드를 입력해주세요.">
			</div>
			<div class="useripok">
			<input class="ipcansel" type="button" value="찾기" id="sendcode">
			</div>
			<br>
			<br>
			<br>
			<br>
			<br>
			<div class=userjoin>
			<a onclick="window.close()" href="./userjoin.jsp" target="_blank">
			<input class="ipjoin" type="button" value="회원가입">
			</a>
			</div>
			<div class="useripcansel">
			<a href="../main/index.jsp"><input class="ipcansel" type="button" value="취소" onclick="window.close()"></a>
			</div>
		</div>
		</form>
</body>
</html>