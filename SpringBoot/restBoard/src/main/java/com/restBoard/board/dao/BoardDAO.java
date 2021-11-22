package com.restBoard.board.dao;

import java.util.List;

import org.mybatis.spring.SqlSessionTemplate;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;

import com.restBoard.board.vo.BoardVO;

@Repository
public class BoardDAO {

	@Autowired
	private SqlSessionTemplate sqlSessionTemplate;
	
	public List<BoardVO> selectList(){
		return sqlSessionTemplate.selectList("boardMapper.selectList");
	}
	
	public void insertBoard(BoardVO vo) {
		sqlSessionTemplate.insert("boardMapper.insertBoard", vo);
	}
	
	public BoardVO getBoard(int seq) {
		return sqlSessionTemplate.selectOne
				("boardMapper.getBoard", seq);
	}
	
	public void cntCount(int seq) {
		sqlSessionTemplate.update("boardMapper.cntCount",seq);
	}

	public void updateBoard(BoardVO vo) {
		// TODO Auto-generated method stub
		sqlSessionTemplate.update("boardMapper.updateBoard",vo);
	}

	public void deleteBoard(int seq) {
		// TODO Auto-generated method stub
		sqlSessionTemplate.delete("boardMapper.deleteBoard",seq);
	}
}