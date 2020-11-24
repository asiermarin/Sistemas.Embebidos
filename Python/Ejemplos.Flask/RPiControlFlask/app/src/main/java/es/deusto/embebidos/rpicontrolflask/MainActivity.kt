package es.deusto.embebidos.rpicontrolflask

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.webkit.WebView
import android.webkit.WebViewClient

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val myWebView = WebView(applicationContext)
        setContentView(myWebView)

        //Aquí introduce la IP (de la coneción de wlan) de tu RPi
        //en la que está corriendo tu servidor web de FLASK
        myWebView.loadUrl("http://192.168.0.12:5000")


        myWebView.webViewClient = WebViewClient()
    }




}