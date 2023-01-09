from bokeh.plotting import figure
from bokeh.io import export_svgs,  show
from flask import Flask, render_template

# # figure를 만들어줍니다.
# p = figure(title="simple line example", x_axis_label='x', y_axis_label='y')
#
# x = [1,2,3,4]
# y1, y2 = [4,3,2,1], [1,2,3,4]
#
# # line으로 그려줍니다.
# p.line(x, y1, legend="Y1", line_width=5, line_color='blue')
# p.line(x, y2, legend="Y2", line_width=2, line_color='red')
#
# ######################
# ## svg로 뽑아줍시다.
# show(p)

app = Flask(__name__)
@app.route('/bokeh_standalone_HTML')
def bokeh_standalone_HTML():
    from bokeh.plotting import figure
    from bokeh.resources import CDN
    from bokeh.embed import file_html

    plot = figure()
    plot.circle([1,2, 5], [3,4, 8], size=20, color="navy", alpha=0.5)
    plot1 = figure()
    plot1.circle([1,2, 5], [3,4, 8], size=20, color="navy", alpha=0.5)
    """
    - models: 어떤 figure를 그릴지 전달합니다. 2개를 전달하면, 연속으로 하나씩 포함되어서 그려지죠. 
    - resources: resource, 즉 Bokeh JS와 CSS assets들을 가져옵니다. 
    - title: html 내의 태그 중에서 <title>에 해당하는 것을 의미합니다. 
    """
    return file_html(models=[plot, plot1], resources=CDN, title="my plot")
if __name__ == '__main__':
    app.run(debug=True)