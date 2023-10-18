//페이징 처리 클래스
package cteam.vo;

public class PageVO 
{
	protected int    pageTotal;   //전체 페이지 갯수
	protected int    blockStart;  //페이지 시작 블럭 
	protected int    blockEnd;    //페이지 종료 블럭
	protected String pgURL;       //페이징 URL 템플릿
	
	//전체 페이지 갯수 설정
	public void SetPgTotal(int dataTotal,int pageNow)
	{
		//전체 게시물 페이지 갯수를 구한다.
		pageTotal = (dataTotal/10);
		//데이터가 10의 배수인 경우
		if(dataTotal % 10 != 0) pageTotal++;
		//페이지 블럭 계산
		SetPgBlock(pageNow);
	}
	
	//페이징 블록 계산
	public void SetPgBlock(int pageNow)
	{
		//페이지 시작 블럭 계산
		blockStart = pageNow - (pageNow % 5) + 1;
		if(pageNow % 5 == 0)
		{
			blockStart = (pageNow - 1) - ((pageNow - 1) % 5) + 1;
		}		
		//페이지 종료 블럭 계산
		blockEnd = blockStart + 5;
		
		//페이지 종료 블럭 값이 전체 페이지 갯수보다 크면...
		if(blockEnd >= pageTotal) blockEnd = pageTotal + 1;		
	}
	
	//페이징 템플릿을 설정한다.
	public void SetPgURL(String url)
	{
		pgURL = url;
	}
	
	//이전 블럭 얻기
	public String GetPrevBlock()
	{
		String url = pgURL;

		if(blockStart > 1)
		{
			url = url.replace("{page}", Integer.toString(blockStart - 1));
		}else
		{
			url = "";
		}
		System.out.println("GetPrevBlock : " + url);
		return url;
	}
	
	//다음 블럭 얻기
	public String GetNextBlock()
	{
		String url = pgURL;

		if(blockEnd < pageTotal)
		{
			url = url.replace("{page}", Integer.toString(blockEnd));
		}else
		{
			url = "";
		}
		System.out.println("GetNextBlock : " + url);
		return url;
	}	
	
	//페이징 얻기
	public String GetPaging(int pageNow)
	{
		String url = "";
		for(int i = blockStart; i < blockEnd; i++)
		{
			url += pgURL.replace("{page}", Integer.toString(i));
			url += "\n";
		}	
		System.out.println("GetPaging : " + url);
		return url;
	}
	
	public String PrintPaging(String pgURL)
	{
		String url = pgURL;
		//이전 블럭
		String urlPrev    = "";
		String urlPgBlock = "";
		String urlNext    = "";
		
		return "";
	}
}
