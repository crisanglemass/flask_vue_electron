// 引入nodejs模块
const {app, BrowserWindow} = require('electron');
const {exec} = require('child_process');
const path = require('path');

// 创建窗口函数
function createWindow() {
    win = new BrowserWindow({ // 设置窗口option
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
        console.log(`Python stdout：${data}`);
    });
    pythonProcess.stderr.on('data', (data) => {
        console.error(`Python error：${data}`);
    });
    win.loadURL('http://127.0.0.1:5000/')// 窗口加载本地html



}


// 初始化函数
function initApp() {
    createWindow();
}


// electron ready 事件触发
app.on('ready', initApp);

// electron 窗口关闭事件触发
app.on('window-all-closed', () => {

    if (process.platform !== 'darwin') {
        app.quit()

    }
});


