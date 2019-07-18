<?php
defined('BASEPATH') OR exit('No direct script access allowed');

class Sn extends CI_Controller {

	public function __construct()
	{
		$this->load->database();
	}

	public function index()
	{
		$this->load->view('sn');
	}






}
