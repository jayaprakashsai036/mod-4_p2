package mod4.project2

import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import androidx.appcompat.app.AppCompatActivity
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView

class MainActivity : AppCompatActivity() {
    private val messages = mutableListOf<String>()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val input = findViewById<EditText>(R.id.messageInput)
        val send = findViewById<Button>(R.id.sendButton)
        val recycler = findViewById<RecyclerView>(R.id.recyclerView)

        val adapter = MessageAdapter(messages)
        recycler.layoutManager = LinearLayoutManager(this)
        recycler.adapter = adapter

        send.setOnClickListener {
            val message = input.text.toString().trim()
            if (message.isNotEmpty()) {
                messages.add("You: $message")
                adapter.notifyItemInserted(messages.lastIndex)
                recycler.scrollToPosition(messages.lastIndex)
                input.text.clear()
            }
        }
    }
}
