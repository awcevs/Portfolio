package cteam.vo;

public class ServiceVO
{
	protected String sno;  //추천신고 번호
	protected String id;   //아이디
	protected String sdiv; //추천 신고 구분
	protected String bno;  //게시글번호
	protected String rno;  //댓글번호
	
	
	public String getSno()	{	return sno;	 	}
	public String getId()	{	return id;	  	}
	public String getSdiv()	{	return sdiv;  	}
	public String getBno()	{	return bno;	  	}
	public String getRno()	{	return rno;	  	}
	
	
	public void setSno(String sno)	{	this.sno = sno;		}
	public void setId(String id)	{	this.id = id;		}
	public void setSdiv(String sdiv){	this.sdiv = sdiv;	}
	public void setBno(String bno)	{	this.bno = bno;		}
	public void setRno(String rno)	{	this.rno = rno;		}
	
	
}
