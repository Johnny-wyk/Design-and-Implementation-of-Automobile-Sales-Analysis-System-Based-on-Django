const base = {
    get() {
        return {
            url : "http://localhost:8080/djangod07x7d4j/",
            name: "djangod07x7d4j",
            // 退出到首页链接
            indexUrl: 'http://localhost:8080/front/dist/index.html'
        };
    },
    getProjectName(){
        return {
            projectName: "汽车销量分析系统"
        } 
    }
}
export default base
