class AyasController < ApplicationController
  before_action :set_aya, only: %i[ show edit update destroy ]

  # GET /ayas or /ayas.json
  def index
    @ayas = Aya
  end

  # GET /ayas/1 or /ayas/1.json
  def show
  end

  def home
  end

  # GET /ayas/new
  def new
    @aya = Aya.new
  end

  # GET /ayas/1/edit
  def edit
  end

  # POST /ayas or /ayas.json
  def create
    @aya = Aya.new(aya_params)

    respond_to do |format|
      if @aya.save
        format.html { redirect_to aya_url(@aya), notice: "Aya was successfully created." }
        format.json { render :show, status: :created, location: @aya }
      else
        format.html { render :new, status: :unprocessable_entity }
        format.json { render json: @aya.errors, status: :unprocessable_entity }
      end
    end
  end

  # PATCH/PUT /ayas/1 or /ayas/1.json
  def update
    respond_to do |format|
      if @aya.update(aya_params)
        format.html { redirect_to aya_url(@aya), notice: "Aya was successfully updated." }
        format.json { render :show, status: :ok, location: @aya }
      else
        format.html { render :edit, status: :unprocessable_entity }
        format.json { render json: @aya.errors, status: :unprocessable_entity }
      end
    end
  end

  # DELETE /ayas/1 or /ayas/1.json
  def destroy
    @aya.destroy

    respond_to do |format|
      format.html { redirect_to ayas_url, notice: "Aya was successfully destroyed." }
      format.json { head :no_content }
    end
  end

  private
    # Use callbacks to share common setup or constraints between actions.
    def set_aya
      @aya = Aya.find(params[:id])
    end

    # Only allow a list of trusted parameters through.
    def aya_params
      params.require(:aya).permit(:content, :number)
    end
end
