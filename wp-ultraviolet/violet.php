<?php
/**
 * @package UltraViolet
 * @version 1.0
 */
/*
Plugin Name: UltraViolet frontend for WordPress
Plugin URI: https://github.com/aadps/ultraviolet
Description: A frontend for UltraViolet, driving frontend form/dashboard and interacting with its mini web service.
Author: Xin Chen
Version: 1.0
Author URI: https://aadps.net/about
*/

//Shortcode [UVForm]
function form_func( $atts ){
	return "in principio erat Verbum";
}
add_shortcode( 'UVForm', 'form_func' );

//Shortcode [UVDashboard]
function dashboard_func( $atts ){
	return "in principio erat Verbum";
}
add_shortcode( 'UVDashboard', 'dashboard_func' );

?>
