class SearchController < ApplicationController
  
  
  def index
    # @page=params.fetch(:page,0).to_i

     @query = Aya.ransack(params[:q])
     @ayas1 = @query.result(distinct: true)
    # @ayas =@ayas1.offset(@page * 10).limit(10)
     @counter= @ayas1.count
    @pagy, @ayas = pagy(@ayas1,items:5)


    # @ayas= Aya.where("text LIKE ?","%" + params[:q] + "%")



  end

  # def past
  #   page:@page - 1
  #   @ayas =@ayas1.offset(@page * 10).limit(10)
  # end

  # def next_page
  #   page:@page + 1
  #   @ayas =@ayas1.offset(@page * 10).limit(10)
  # end

end
