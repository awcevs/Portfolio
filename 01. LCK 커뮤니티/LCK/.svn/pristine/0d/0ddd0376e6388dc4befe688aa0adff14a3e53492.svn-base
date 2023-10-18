package test;

import java.util.ArrayList;

import cteam.dao.*;
import cteam.dto.*;
import cteam.dto.*;
import cteam.vo.*;

public class Test
{
	
	public static void main(String[] args) 
	{
		BoardDTO dto = new BoardDTO();
		BoardVO vo = new BoardVO();
		
		/*
		for (int i = 0; i < 5; i++)
		{
			vo.setBtitle("제목 " + i);
			vo.setBnote("검색 테스트");
			vo.setMenu("F");
			vo.setId("admin");
			dto.Insert(vo);
		}
		*/
		
		ArrayList<BoardVO> list = dto.List("F");
		for(BoardVO avo : list)
		{
			System.out.println(avo.getBtitle());
		}
	}
	
	
}
