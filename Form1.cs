using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO;

namespace MR.PATROL11
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Button1_Click(object sender, EventArgs e)
        {
            webBrowser1.Navigate("orange.gps-trace.com/");
        }

        private void Button2_Click(object sender, EventArgs e)
        {
            string WebPage = textBox1.Text.Trim();
            webBrowser2.Navigate(WebPage);
        }
        private void Button3_Click(object sender, EventArgs e)
        {
            timer1.Start();
        }

        private void Timer1_Tick(object sender, EventArgs e)
        {
            FileStream fstream = new FileStream(@"F:\FYP\emer res\result\result.txt", FileMode.Open, FileAccess.Read, FileShare.ReadWrite);

            TextReader reader = new StreamReader(fstream);
            richTextBox1.Text = reader.ReadToEnd();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            
        }
    }
}
