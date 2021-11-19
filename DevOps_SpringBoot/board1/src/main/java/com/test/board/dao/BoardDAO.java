package com.test.board.dao;

import java.util.List;

import org.mybatis.spring.SqlSessionTemplate;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;

import com.test.board.vo.BoardVO;

@Repository
public class BoardDAO {

	@Autowired
	private SqlSessionTemplate sqlSessionTemplate;
	
	public List<BoardVO> selectList(){
		return sqlSessionTemplate.selectList("boardMapper.selectList");
	}
}
