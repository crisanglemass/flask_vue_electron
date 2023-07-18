// ����nodejsģ��
const {app, BrowserWindow} = require('electron');
const {exec} = require('child_process');
const path = require('path');

// �������ں���
function createWindow() {
    win = new BrowserWindow({ // ���ô���option
        width: 800,
        height: 600,
        webPreferences: {
            nodeIntegration: true,
            contextIsolation: false,
            enableRemoteModule: true
        }
    });
    const pythonProcess = exec('venv\\Scripts\\python app.py');
    pythonProcess.stdout.on('data', (data) => {
        console.log(`Python stdout��${data}`);
    });
    pythonProcess.stderr.on('data', (data) => {
        console.error(`Python error��${data}`);
    });
    win.loadURL('http://127.0.0.1:5000/')// ���ڼ��ر���html



}


// ��ʼ������
function initApp() {
    createWindow();
}


// electron ready �¼�����
app.on('ready', initApp);

// electron ���ڹر��¼�����
app.on('window-all-closed', () => {

    if (process.platform !== 'darwin') {
        app.quit()

    }
});


