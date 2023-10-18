package cteam.dao;

import java.util.Properties;

import javax.mail.Authenticator;
import javax.mail.Message;
import javax.mail.PasswordAuthentication;
import javax.mail.Session;
import javax.mail.Transport;
import javax.mail.internet.InternetAddress;
import javax.mail.internet.MimeMessage;

public class MailSender 
{
	public boolean MailSend(String from,String to,String id,String pw,String title,String body)
	{
		try
		{  
			System.out.println("send stage 01");
			
			Properties clsProp = System.getProperties();
			
			// 메일 서버 주소
			clsProp.put( "mail.smtp.host", "smtp.naver.com" );
			
			// 메일 서버 포트 번호
			clsProp.put( "mail.smtp.port", 465 );			
			
			System.out.println("send stage 02");
			
			// 인증이 필요하면 아래와 같이 설정한다.
			clsProp.put("mail.smtp.auth", "true"); 
			clsProp.put("mail.smtp.ssl.enable", "true"); 
			clsProp.put("mail.smtp.ssl.trust", "smtp.naver.com");			
			
			System.out.println("send stage 03");
			
			Session clsSession = Session.getInstance( clsProp, new Authenticator(){
					public PasswordAuthentication getPasswordAuthentication()
					{
						// 인증 아이디/비밀번호를 저장한다.
						return new PasswordAuthentication( id, pw );
					}
				} );
			
			System.out.println("send stage 04");
			
			Message clsMessage = new MimeMessage( clsSession );
			
			// 발신자 이메일 주소를 설정한다.
			clsMessage.setFrom( new InternetAddress( from ) );
			
			System.out.println("send stage 05");
			
			// 수신자 이메일 주소를 설정한다.
			clsMessage.addRecipient( Message.RecipientType.TO, new InternetAddress( to ) );
			
			System.out.println("send stage 06");
			
			// 제목을 저장한다.
			clsMessage.setSubject( title );
			
			// 메일 내용을 저장한다. 소스 코드를 euc-kr 로 작성하여서 charset 을 euckr 로 설정함.
			clsMessage.setContent( body , "text/html;charset=euckr" );
			
			System.out.println("send stage 07");
			
			// 메일 전송
			Transport.send( clsMessage );
			
			
			System.out.println("send stage 08");
		}
		catch( Exception e )
		{
			e.printStackTrace();
			return false;
		}		
		return true;
	}
	
	public static void main(String[] args) 
	{
		
		MailSender m = new MailSender();
		m.MailSend("rkdckdgml119@naver.com", 
				"rkdckdgml119@naver.com",
				"rkdckdgml119","ckdgml0926!",
				"this is title","this is body");
		
		
		//MailSender 클래스를 아래와 같이 구조를 변경하여 고쳐 쓸것!!!!!!!!!!
		
		/*
		MailSender send = new MailSender();
		send.setFrom("rkdckdgml119@naver.com","rkf");
		send.setTo("test@gmail.com");
		send.setTitle("이것은 제목입니다.");
		send.setBody("<a href='autho.jsp?id=121212'>인증하기</a>");
		send.sendMail();	
		*/
	}

}

