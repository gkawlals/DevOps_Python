package com.restBoard.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.restBoard.dao.BoardDAO;
import com.restBoard.vo.BoardVO;

@Service
public class BoardService {
	@Autowired
	BoardDAO dao;
	
	public List<BoardVO> selectList(){
		return dao.selectList();
	}
	
	public void insertBoard(BoardVO vo) {
		dao.insertBoard(vo);
	}
	
	public BoardVO getBoard(int seq) {
		dao.cntCount(seq);
		return dao.getBoard(seq);
	}
	
	public BoardVO updateBoard(int seq) {
		return dao.getBoard(seq);
	}

	public void updateBoard(BoardVO vo) {
		// TODO Auto-generated method stub
		dao.updateBoard(vo);
	}

	public void deleteBoard(int seq) {
		// TODO Auto-generated method stub
		dao.deleteBoard(seq);
	}
}
