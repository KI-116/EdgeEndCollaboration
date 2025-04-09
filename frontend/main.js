const { app, BrowserWindow } = require("electron");

let mainWindow;

app.whenReady().then(() => {
    // 创建 Electron 窗口
    mainWindow = new BrowserWindow({
        width: 800,
        height: 600,
        webPreferences: {
            nodeIntegration: false, // 禁用 Node 集成，提高安全性
            contextIsolation: true,
        },
    });

    // 加载远程 Flask 服务器页面
    mainWindow.loadURL("http://211.86.155.109:5000");  // 替换为 Flask 服务器的实际 IP 地址和端口

    mainWindow.on("closed", () => {
        mainWindow = null;
    });
});

app.on("window-all-closed", () => {
    if (process.platform !== "darwin") {
        app.quit();
    }
});
