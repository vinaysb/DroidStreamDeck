package com.example.vinay.droidstreamdeck;

import android.os.AsyncTask;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.EditText;
import android.widget.Toast;
import java.io.IOException;
import java.io.PrintWriter;
import java.net.Socket;

public class MainActivity extends AppCompatActivity {
    EditText ip_addr;
    EditText port;
    String mess = null;
    String ip = null;
    int port_num = 0;
    ConnParams params = null;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.deck);

        ip_addr=findViewById(R.id.ip);
        port=findViewById(R.id.port);
    }

    static class ConnParams{
        String ip;
        String message;
        int port;
        ConnParams(String ip, int port, String message){
            this.ip = ip;
            this.port = port;
            this.message = message;
        }
    }

    public void connect (View v){
        switch (v.getId()){
            case R.id.conn:
                mess = "Conn";
                ip = ip_addr.getText().toString();
                port_num = Integer.parseInt(port.getText().toString());
                Toast.makeText(getApplicationContext(), "Connection Sent", Toast.LENGTH_LONG).show();
                break;
            case R.id.B0:
                mess = "0";
                break;
            case R.id.B1:
                mess = "1";
                break;
            case R.id.B2:
                mess = "2";
                break;
            case R.id.B3:
                mess = "3";
                break;
            case R.id.B4:
                mess = "4";
                break;
            case R.id.B5:
                mess = "5";
                break;
            case R.id.B6:
                mess = "6";
                break;
            case R.id.B7:
                mess = "7";
                break;
            case R.id.B8:
                mess = "8";
                break;
            case R.id.B9:
                mess = "9";
                break;
                default:
                    Toast.makeText(getApplicationContext(), "Button Not Ready :)", Toast.LENGTH_SHORT).show();
                    break;
        }
        if(ip != null && port_num != 0){
            params = new ConnParams(ip, port_num, mess);
            ServerConnection sc = new  ServerConnection();
            sc.execute(params);
        }
        else{
            Toast.makeText(getApplicationContext(), "Please enter correct IP and Port and hit on connect", Toast.LENGTH_LONG).show();
        }

    }
}

class ServerConnection extends AsyncTask<MainActivity.ConnParams, Void, Void> {

    @Override
    protected Void doInBackground(MainActivity.ConnParams... params)
    {
        String ip = params[0].ip;
        int port = params[0].port;
        String message = params[0].message;
        try
        {
            Socket socket = new Socket(ip, port);
            PrintWriter printWriter = new PrintWriter(socket.getOutputStream());
            printWriter.write(message);
            printWriter.flush();
            printWriter.close();
            socket.close();
        } catch (IOException e){
            e.printStackTrace();
        }
        return null;
    }
}