<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ page import="cteam.dao.*" %>
<%@ page import="cteam.dto.*" %>
<%@ page import="cteam.vo.*" %>
<%@ page import="java.util.*" %>
<%
%>
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Insert title here</title>
<script src="../js/jquery-3.7.0.js"></script>
</head>
<body>
	<style>
	.userjoin_form
	{
    	width: 400px;
	    margin: auto; 
	    padding: 0 20px;
	    margin-bottom: 20px;
	}
	
	
	.userjoin_form.fild
	{
		margin:5px 0;
	}
	
	
	.userjoin_form b
	{
	    display: block; 
	    margin-bottom: 5px;
	}
	
	.userjoin_form input:not(input[type=test]),.userjoin_form select
	{
	    border: 1px solid #dadada;
	    padding: 15px;
	    width: 100%;
	    margin-bottom: 5px;
	}
	
	.userjoin_form input[type=button],
	.userjoin_form input[type=submit]
	{
	}
	
	.userjoin_form.fild_team div
	{ 
	    display: flex;
	    gap:10px; 
	}
	
	.fild.tel-number div 
	{
    	display: flex;
	}
	
	.fild.tel-number div input:nth-child(1)
	{
    	flex:2;
 	}

	.fild.tel-number div input:nth-child(2)
	{
    	flex:1;
	}
	
	.fild_team
	{
    	width: 430px;
	    margin: auto;
	    margin-bottom: 20px;
	}
	
	.fild_pt
	{
		width: 430px;
	    margin: auto; 
	    margin-bottom: 20px;
	}
	
	.joinok
	{
		width:33%; 
		float:left;
		/*border: 1px solid gold; 
		float: left; 
		width: 33%;"
		*/
	}
	.joincansel
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
	//아이디  중복 검사 상태를 저장하기 위한 변수
	//ERROR / DUPLICATE / NOT_DUPLICATE
	
	var checkCode = "ERROR";
	
	//닉네임 중복 검사
	var nickcheckCode = "오류";
	
	$(document).ready(function(){
		
		
		//alert("test");
		
		//발송 button id 값
		$("#sendCode").click(function(){
			
			 //alert("tet");
			 
			 //!email_check -> 이메일 형식 체크 코드
			var usermail = 	$("#usermail").val();
			if(!email_check(usermail))
			{
				alert("이메일 형식에 맞게 입력해주세요");
				return false;
			}
			var code="";
			$.ajax({
				type : "post",
				url: "emailcode.jsp",
				data: {"usermail": usermail},
				dataType: "html", //html,xml,json 셋 중 데이터 타입을 정할 수 있음
				success : function(data) 
				{
					data = data.trim();
					console.log(data);
					//데이터베이스에 이미 가입되어있는 이메일이 있을 시 가입 방지
					if(data == "중복된 이메일")
					{
						alert("이미 가입되어있는 이메일 입니다.");
						$("#usermail").focus();
						return false;
					}else
					{
						//alert(data.length);
						//가입되어있는 이메일이 아닐 때 코드를 보냄
						code ="<%=session.getAttribute("code")%>";
				
						alert("이메일로 인증코드를 보냈습니다.");
					}
				},
				error : function(){
					alert("인증코드 전송 오류입니다");
				}
			});				
		});
		$("#userid").focus();
		
		//아이디 입력시 이벤트
		$("#userid").keyup(function(){
			DuplicateCheckID();
			//alert("완료");
		});
		//닉네임 입력시 이벤트
		$("#user").keyup(function(){
			DuplicateCheckNICK();
		});
		
		//폼 전송시 이벤트
		$("#userjoinFrm").submit(function(){
		
			if(checkCode == "DUPLICATE")
			{
				alert("중복된 회원아이디 입니다. 회원가입을 진행 할 수 없습니다.");
				return false;
			}
			
			if(nickcheckCode == "중복")
			{
				alert("중복된 회원닉네임 입니다. 회원가입을 진행 할 수 없습니다.");
				return false;
			}
			
			if( $("#userid").val() == "")
			{
				alert("아이디를 입력하세요.");
				$("#userid").focus();
				return false;
			}
			if( $("#userpw").val() == "")
			{
				alert("비밀번호를 입력하세요.");
				$("#userpw").focus();
				return false;
			}	
			if( $("#userpw").val() != $("#userpwcheck").val())
			{
				alert("비밀번호가 일치하지 않습니다.");
				$("#userpw").focus();
				return false;
			}	
			if( $("#username").val() == "")
			{
				alert("이름을 입력하세요.");
				$("#username").focus();
				return false;
			}
			if( $("#user").val() == "")
			{
				alert("닉네임을 입력하세요.");
				$("#user").focus();
				return false;
			}
			
			if( $("#usermail").val() == "")
			{
				alert("이메일을 입력하세요.");
				$("#user").focus();
				return false;
			}
			
			if( $("#userok").val() == "")
			{
				alert("인증코드를 입력해주세요");
				$("#userok").focus();
				return false;
			}
			
			//세션에 구워져있는 코드 비교 검사 ajax
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
					//세션에 구워져있는 코드가 일치하지 않으면 가입 안됨
					if($("#userok").val() != data)
					{
						alert("가입코드가 일치 하지 않습니다.");
						$("#userok").focus();
					}else
					{
						//맞으면 가입 진행
						if(confirm("회원가입을 진행하시겠습니까?") == true)
						{
							//$("#joinFrm").submit();
							document.userjoinFrm.submit();
							return true;
						}
					}
				},
				error : function(xhr, status, error) 
				{
					// 통신 오류 발생시
				}
			});
			return false;
		});
	});
	
	
	//이메일 형식 체크 검사
	function email_check(usermail) {

		var reg = /^[0-9a-zA-Z]([-_\.]?[0-9a-zA-Z])*@[0-9a-zA-Z]([-_\.]?[0-9a-zA-Z])*\.[a-zA-Z]{2,3}$/i;

		return reg.test(usermail);

	}
	
	//특수문자 체크 검사
	function characterCheck(obj)
	{
	    var regExp = /[\{\}\[\]\/?.,;:|\)*~`!^\-_+<>@\#$%&\\\=\(\'\"]/g;
	   	var regex = /(?:[\u2700-\u27bf]|(?:\ud83c[\udde6-\uddff]){2}|[\ud800-\udbff][\udc00-\udfff]|[\u0023-\u0039]\ufe0f?\u20e3|\u3299|\u3297|\u303d|\u3030|\u24c2|\ud83c[\udd70-\udd71]|\ud83c[\udd7e-\udd7f]|\ud83c\udd8e|\ud83c[\udd91-\udd9a]|\ud83c[\udde6-\uddff]|\ud83c[\ude01-\ude02]|\ud83c\ude1a|\ud83c\ude2f|\ud83c[\ude32-\ude3a]|\ud83c[\ude50-\ude51]|\u203c|\u2049|[\u25aa-\u25ab]|\u25b6|\u25c0|[\u25fb-\u25fe]|\u00a9|\u00ae|\u2122|\u2139|\ud83c\udc04|[\u2600-\u26FF]|\u2b05|\u2b06|\u2b07|\u2b1b|\u2b1c|\u2b50|\u2b55|\u231a|\u231b|\u2328|\u23cf|[\u23e9-\u23f3]|[\u23f8-\u23fa]|\ud83c\udccf|\u2934|\u2935|[\u2190-\u21ff])/g;
	    if(regExp.test(obj.value)){
	        alert("특수문자는 입력할 수 없습니다.");
	        obj.value = "";
	    }
	    if(regex.test(obj.value))
	    {
	        alert("입력 불가능한 문자 입니다.");
	        obj.value = "";
	    }
	}
	
	//아이디 입력란에 한글이나 특수문자 체크 검사
	function idpwCheck(obj){
	    var regExp = /[^0-9a-zA-Z]/g;
	    if(regExp.test(obj.value)){
	        alert("한글이나 특수문자는 입력할 수 없습니다.");
	        obj.value = "";
	    }
	}
	
	
	
	


	
	
	//아이디 중복검사
	function DuplicateCheckID()
	{
		checkCode = "ERROR";
		
		userID = $("#userid").val();
		if(userID == "")
		{
			$("#msg").html("아이디를 입력하세요.");
			return;
		}
		
		//아이디 중복검사 ajax 호출
		$.ajax({
			type : "get",
			url: "useridcheck.jsp?userid=" + userID,
			dataType: "html",
			success : function(data) 
			{	
				// 통신이 성공적으로 이루어졌을때 이 함수를 타게된다.
				data = data.trim();
				//ERROR / DUPLICATE / NOT_DUPLICATE
				console.log(data);
				checkCode = data;
				//alert("완료");
				switch(data)
				{
				case "ERROR":
					$("#msg").html("아이디 중복검사 오류입니다.");
					break;
				case "DUPLICATE":
					$("#msg").html("<span style='color:red'>중복된 아이디입니다.</span>");
					break;		
				case "NOT_DUPLICATE":
					$("#msg").html("사용 가능한 아이디입니다.");
					break;					
				}
			},
			error : function(xhr, status, error) 
			{
				// 통신 오류 발생시
				console.log(data);
			}
		});			
	}
	
	//닉네임 중복검사 함수
	function DuplicateCheckNICK()
	{
		nickcheckCode = "오류";
		
		userNICK = $("#user").val();
		if(userNICK == "")
		{
			$("#nickmsg").html("닉네임을 입력하세요.");
			return;
		}
		
		$.ajax({
			type : "get",
			url: "usernickcheck.jsp?user=" + userNICK,
			dataType: "html",
			contentType : "application/html; charset:UTF-8",
			success : function(data) 
			{	
				// 통신이 성공적으로 이루어졌을때 이 함수를 타게된다.
				data = data.trim();
				//오류 / 중복 / 중복안됨
				console.log(data);
				nickcheckCode = data;
				//alert("완료");
				switch(data)
				{
				case "오류":
					$("#nickmsg").html("닉네임 중복검사 오류입니다.");
					break;
				case "중복":
					$("#nickmsg").html("<span style='color:red'>중복된 닉네임입니다.</span>");
					break;		
				case "중복안됨":
					$("#nickmsg").html("사용 가능한 닉네임입니다.");
					break;					
				}
			},
			error : function(xhr, status, error) 
			{
				// 통신 오류 발생시
				console.log(data);
			}
		});			
	}
		
	</script>
	<form id="userjoinFrm" name="userjoinFrm" method="post" action="userjoinok.jsp">
		<div style="display:flex;">
			<div style="float:left;vertical-align:middle;  position: absolute; top: 50%; right:70%;transform: translate(0, -50%);">
				<a href="../main/index.jsp" style="float:left"><img src="../images/logo2.png"></a>
			</div>
			<div class="userjoin_form" style="float:left">
				<div class="fild">
				<b>아이디(*)</b>
				<input maxlength="20" class="userid" type="text" id="userid" name="userid" placeholder="아이디를 입력해주세요.(최대 20글자)" onkeyup="idpwCheck(this)" onkeydown="idpwCheck(this)">
				<span id="msg">아이디를 입력하세요.</span>
				</div>
				<div class="fild">
				<b>비밀번호(*)</b>
				<input maxlength="20" class="userpw" type="password" id="userpw" name="userpw" placeholder="비밀번호를 입력해주세요.(최대 20글자)">
				</div>
				<div class="fild">
				<b>비밀번호 확인(*)</b>
				<input maxlength="20" class="userpwcheck" type="password" id="userpwcheck" name="userpwcheck" placeholder="비밀번호를 다시 한번 입력해주세요.(최대 20글자)">
				</div>
				<div class="fild">
				<b>이름(*)</b>
				<input maxlength="6" class="username" id="username" name="username" placeholder="(최대 6글자)" onkeyup="characterCheck(this)" onkeydown="characterCheck(this)">
				</div>
				<div class="fild">
				<b>닉네임(*)</b>
				<input maxlength="6" class="user" id="user" name="user" placeholder="(최대 6글자)" onkeyup="characterCheck(this)" onkeydown="characterCheck(this)">
				<span id="nickmsg">닉네임을 입력하세요.</span>
				</div>
				<div class="fild_team">
				<b>응원하는 팀(*)</b>
					<select name="userteam" id="userteam" class="fild_team">
							<option selected>T1</option>
							<option >BRO</option>
							<option >DK</option>
							<option >DRX</option>
							<option >GENG</option>
							<option >HLE</option>
							<option >KDF</option>
							<option >KT</option>
							<option >LSB</option>
							<option >NS</option>
							</select>
				</div>
				<div class="fild_pt">
				<b>주 포지션(*)</b>
					<select name="userpt" id="userpt" class="fild_pt">
						<option selected>TOP</option>
						<option >MID</option>
						<option >JUG</option>
						<option >AD</option>
						<option >SUP</option>
					</select>
				</div>
				<div class="fild">
				<b>이메일(*)</b>
					<input class="usermail" id="usermail" name="usermail" placeholder="ex) ezen123@naver.com" ><input type="button" value="발송" id="sendCode">
				</div>
				<div class="fild">
				<b>인증코드(*)</b>
					<input class="userok" id="userok" name="userok" placeholder="인증코드를 입력해주세요.">
				</div>
				<div class=joinok>
					<input class="joinok" type="submit" value="가입하기">
				</div>
				<div class="joincansel">
					<a href="../main/index.jsp"><input class="joincansel" type="button" value="취소"></a>
				</div>
			</div>
		</div>
	</form>
</body>
</html>