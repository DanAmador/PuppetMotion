using Communicator;
using UnityEngine;
using UnityEngine.UI;

public class ConnectorView : MonoBehaviour {
    private SocketComponent socketComponent;

    private InputField host, port;

    void Start() {
        socketComponent = FindObjectOfType<SocketComponent>();
        if (socketComponent == null) {
            Debug.LogError("Cannot find the socket component");
        }
        else {
            InitializeChildren();
        }
    }

    private void InitializeChildren() {
        Transform aux;

        aux = transform.Find("Host");
        if (aux == null) {
            Debug.LogError("Cannot find the host text object");
        }
        else {
            host = aux.GetComponent<InputField>();
            host.text = socketComponent.host;
        }

        aux = transform.Find("Port");
        if (aux == null) {
            Debug.LogError("Cannot find the port text object");
        }
        else {
            port = aux.GetComponent<InputField>();
            port.text = socketComponent.port.ToString();
        }
    }

    public void Connect() {
        try {
            socketComponent.SetUpConnection(host.text, int.Parse(port.text));
        }
        catch {
            Debug.LogError($"Unable to find ws://{host.text}:{port.text}");
        }
    }
}