using Communicator;
using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class ConnectorView : MonoBehaviour
{
    private SocketComponent socketComponent;

    private InputField host, port;

    // Start is called before the first frame update
    void Start()
    {
        socketComponent = FindObjectOfType<SocketComponent>();
        if ((object)socketComponent == null)
        {
            Debug.LogError("Cannot find the socket component");
        }
        else
        {
            InitializeChildren();
        }
    }

    private void InitializeChildren()
    {
        Transform aux;

        aux = this.transform.Find("Host");
        if ((object)aux == null)
        {
            Debug.LogError("Cannot find the host text object");
        }
        else
        {
            host = aux.GetComponent<InputField>();
            host.text = socketComponent.host;
        }

        aux = this.transform.Find("Port");
        if ((object)aux == null)
        {
            Debug.LogError("Cannot find the port text object");
        }
        else
        {
            port = aux.GetComponent<InputField>();
            port.text = socketComponent.port.ToString();
        }
    }

    public void Connect()
    {
        socketComponent.NewConnection(
            host.text,
            int.Parse(port.text)
            );
    }
}
