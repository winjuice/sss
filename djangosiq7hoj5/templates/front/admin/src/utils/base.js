const base = {
    get() {
        return {
            url : "http://localhost:8080/djangosiq7hoj5/",
            name: "djangosiq7hoj5",
            // 退出到首页链接
            indexUrl: 'http://localhost:8080/front/dist/index.html'
        };
    },
    getProjectName(){
        return {
            projectName: "基于网络爬虫的考研信息共享平台的设计与实现"
        } 
    }
}
export default base
