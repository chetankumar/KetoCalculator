from data_reader import DataReader
import torch
import torch.optim as optim
from torch.autograd import Variable


dr = DataReader()
recommended_df = dr.LoadData("recommended.csv")

recipies_df = dr.LoadData("recipies.csv")

recipies_df.set_index('Recipe',inplace=True)

rcp_data = recipies_df.transpose().values
rdd_data = recommended_df["Recommended"].T.values

rcp_data = torch.Tensor(rcp_data)
rdd_data = torch.Tensor(rdd_data)
rcp_amounts = Variable(torch.randn(rcp_data.size()[1]),requires_grad=True)
rcp_recipe_ingredients = Variable(torch.randn(rcp_data.size()),requires_grad=True)

optimizer = optim.SGD([rcp_amounts,rcp_recipe_ingredients],lr=0.0001)

for t in range(10000):

    tmp_recipe = rcp_data * rcp_recipe_ingredients
    output = torch.matmul(tmp_recipe,rcp_amounts)
    loss = (rdd_data - output).pow(2).sum()
    loss.backward()
    optimizer.step()
    rcp_amounts.grad.data.zero_()
    rcp_recipe_ingredients.grad.data.zero_()
    rcp_amounts.data.clamp_(0)
    rcp_recipe_ingredients.data.clamp_(0)

    if t % 100 == 0:
        print("{}\t{}".format(t,loss))

print(rcp_amounts)
print(rcp_recipe_ingredients * rcp_data )



