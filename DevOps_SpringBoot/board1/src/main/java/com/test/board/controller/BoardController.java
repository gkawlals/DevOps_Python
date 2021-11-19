package com.test.board.controller;

import java.sql.Date;
import java.util.ArrayList;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;

import com.test.board.dao.BoardDAO;
import com.test.board.vo.BoardVO;

@Controller
public class BoardController {
	@Autowired
	BoardDAO dao;
	
	@RequestMapping("boardlist")
	public String boardList(Model model) {
		List<BoardVO> boardList = dao.selectList();
		model.addAttribute("boardList", boardList);
		return "board/boardlist";
	}
}
