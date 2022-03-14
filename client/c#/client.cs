using System;
using System.Net;
using System.Net.Sockets;

namespace always_run_legacy_server
{
    class Core
    {
        public static string ip = "";
        public static int port = 0;

        public static IPEndPoint client_endpoint;
        public static Socket client_socket;

        static void Main ()
        {
            Console.Write("DIGITE IP PARA CONECTAR: ");
            ip = Console.ReadLine();
            Console.WriteLine("\nRESPONDA COM 's' PARA SIM OU 'qualquer coisa' PARA NÃO!");
            Console.Write("CONVERTER URL EM IP? ");
            string convert = Console.ReadLine();
            if(convert == "s")
            {
                ip = Dns.GetHostEntry(ip).AddressList[0].ToString();
            }
            Console.Write("\nDIGITE PORTA PARA CONECTAR: ");
            port = int.Parse(Console.ReadLine());
            Console.WriteLine("\nTENTANDO CONEXÃO COM: " + ip + ":" + port);
            try
            {
                client_endpoint = new IPEndPoint(IPAddress.Parse(ip), port);
                client_socket = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);
                client_socket.Connect(client_endpoint);
                Console.WriteLine("CONECTADO!");
            }
            catch(System.Exception)
            {
                Console.WriteLine("NÃO FOI POSSÍVEL CONECTAR-SE");
                Console.ReadLine();
                return;
            }
            //encode e envio
            Console.Write("\nESCREVA UMA MENSAGEM: ");
            string message = Console.ReadLine();
            byte[] byData = System.Text.Encoding.ASCII.GetBytes(message);
            client_socket.Send(byData);
        }
    }
}
