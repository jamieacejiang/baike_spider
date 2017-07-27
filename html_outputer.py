# coding:utf8

class HtmlOutputer(object):
    
    def __init__(self):
        self.datas = []
    
    #用于收集数据
    def collect_data(self,data):
        if data is None:
            return
        self.datas.append(data)

    #用于把收集好的数据放到一个html页面中
    def output_html(self):
        fout = open('output.html','w')#写模式
        
        fout.write('<html>')
        fout.write('<body>')
        fout.write('<table>')
        
        for data in self.datas:
            fout.write('<tr>')
            fout.write('<td>%s</td>' % data['url'])
            fout.write('<td>%s</td>' % data['title'].encode('utf-8'))#默认是ascii，不这样写中文可能会乱码
            fout.write('<td>%s</td>' % data['summary'].encode('utf-8'))
            fout.write('</tr>')
        
        fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')
        
        
        fout.close()
    
    
    
    



